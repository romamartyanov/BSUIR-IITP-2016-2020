using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Emulator
{
	public class ALU
	{
		private string running = "";
		public string Add(string op1, string op2, ref Dictionary<string, bool> flags)
		{
			if (running == "")
			{
				Console.WriteLine(op1);
				Console.WriteLine("+");
				Console.WriteLine(op2);
				Console.WriteLine(new string('-', 16));
			}

			
			int len = op1.Length, rem = 0;
			if (op2[0] == '0') Swap(ref op1, ref op2);
			string res = "";
			for (int i = len - 1; i >= 0; i--)
			{
				int cur = Convert.ToInt32(op1[i]) + Convert.ToInt32(op2[i]) - 96 + rem;
				rem = cur / 2;
				res += cur % 2;
				if (cur % 2 == 1 && running == "")
				{
					Console.WriteLine(Interpreter.Normalize(res, 16) + "\t|\tStep " + (op2.Length - i).ToString() +
						", Cur res=" + Interpreter.Normalize(res, 16).TrimStart('0'));
				}
			}

			
			res = new string(res.ToCharArray().Reverse().ToArray());
			if (rem != 0)
			{
				flags["cf"] = true;
				if (running == "mul")
				{
					flags["zf"] = true;
					flags["of"] = true;
				}
			}
			if (!IsNeg(op1) && !IsNeg(op2))
			{
				res = "0" + res.Substring(1, len - 1);
			}
			if (IsNeg(op1) && IsNeg(op2))
			{
				res = "1" + res.Substring(1, len - 1);
			}
			if (running == "")
			{
				Console.WriteLine(new string('-', 16));
				Console.WriteLine("Answer: " + Interpreter.Normalize(res, 16).TrimStart('0') 
					+ "(" + Convert.ToInt32(res, 2) + ")");
			}
			return res;
		}

		public string Sub(string op1, string op2, ref Dictionary<string, bool> flags)
		{
			return Add(op1, Neg(op2, ref flags), ref flags);
		}

		public string Mul(string op1, string op2, ref Dictionary<string, bool> flags)
		{
			running = "mul";
			Console.WriteLine(op1);
			Console.WriteLine('*');
			Console.WriteLine(op2);
			Console.WriteLine(new string('-', 16));
			string res = Interpreter.Normalize("", 100);
			for (int i = op2.Length - 1; i >= 0; i--)
			{
				if (op2[i] == '1')
				{
					res = Add(res, Interpreter.Normalize(op1 + new string('0', op2.Length - i - 1), 100), ref flags);
					Console.WriteLine(Interpreter.Normalize(op1 + new string('0', op2.Length - i - 1), 16)
						+ "\t|\tStep " + (op2.Length - i).ToString() + ", Cur res=" + Interpreter.Normalize(res, 16).TrimStart('0'));
				}
			}
			Console.WriteLine(new string('-', 16));
			Console.WriteLine("Answer: " + Interpreter.Normalize(res, 16).TrimStart('0')
				+ "(" + Convert.ToInt32(res, 2) + ")");
			running = "";
			return res;
		}

		public string Div(string op1, string op2, ref Dictionary<string, bool> flags)
		{
			running = "div";
			Console.WriteLine(op1 + "\t|\t" + op2);
			string tmp = "", ans = "", tmpTrimmed = "";
			for (int i = 0; i < op1.Length; i++)
			{
				tmp += op1[i];
				if (Convert.ToInt32(tmp, 2) < Convert.ToInt32(op2, 2))
				{
					ans += '0';
				}
				else
				{
					tmpTrimmed = tmp.TrimStart('0');
					int real_len = tmpTrimmed.Length;
					Console.Write(new string(' ', i - tmpTrimmed.Length + 1) + op2.TrimStart('0') + '\n');
					
					tmp = Sub(Interpreter.Normalize(tmp, 16), op2, ref flags);
					Console.WriteLine(new string(' ', i - tmpTrimmed.Length + 1) + new string('-', tmpTrimmed.Length));
					Console.Write(new string(' ', i - tmpTrimmed.Length + 1) + tmp.Substring(tmp.Length - real_len,real_len) + '\n');
					
					ans += '1';
					if (tmp.TrimStart('0') == "") tmp = "";
				}
			}
			tmpTrimmed = tmp.TrimStart('0');
			if (tmpTrimmed == "") tmpTrimmed = "0";
			Console.Write("Remainder= " + new string(' ', op1.Length - tmpTrimmed.Length) + tmpTrimmed + '\n');
			Console.WriteLine("Answer: " + Interpreter.Normalize(ans, 16).TrimStart('0')
				+ "(" + Convert.ToInt32(ans, 2) + ")");
			running = "";
			return Interpreter.Normalize(ans, 16);
		}

		public string Inc(string s, ref Dictionary<string, bool> flags)
		{
			if (running == "") running = "Inc";
			string res = "";
			res = Add(s, Interpreter.Normalize("1", 16), ref flags);
			if (running == "Inc") running = "";
			return res;
		}

		private int Abs(string val)
		{
			int x = 0;
			if (IsNeg(val))
			{
				x = 65536 - Convert.ToInt32(val, 2) - 1;
			}
			else x = Convert.ToInt32(val, 2);
			return x;
		}

		private bool IsNeg(string binNum)
		{
			return binNum[0] == '1';
		}

		private void Swap(ref string str1, ref string str2)
		{
			var temp = str2;
			str2 = str1;
			str1 = temp;
		}

		public string Neg(string op1, ref Dictionary<string, bool> flags)
		{
			string res = "";
			foreach (char c in op1)
			{
				if (c == '0') res += '1';
				else res += '0';
			}
			return Inc(res, ref flags);
		}
	}
}
