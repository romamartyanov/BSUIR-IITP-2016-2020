using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuadraticCoprocessor
{
	public static class Processor
	{
		private static Dictionary<string, Register> registers;
		private static Dictionary<string, bool> flags;
		private static ALU alu;
		private static ProcessorState state = ProcessorState.NotStarted;
		private static bool print = true;

		public static Dictionary<string, Register> Registers { get => registers; }
		public static Dictionary<string, bool> Flags { get => flags; }
		public static ProcessorState State => state;

		public static void Start()
		{
			registers = new Dictionary<string, Register>();
			flags = new Dictionary<string, bool>();
			alu = new ALU();
			registers["ax"] = new Register(0);
			registers["bx"] = new Register(0);
			registers["cx"] = new Register(0);
			registers["dx"] = new Register(0);
			registers["si"] = new Register(0);
			registers["bp"] = new Register(0);
			registers["ip"] = new Register(0);

			flags["cf"] = false;
			flags["pf"] = false;
			flags["af"] = false;
			flags["zf"] = false;
			flags["sf"] = false;
			flags["tf"] = false;
			flags["if"] = false;
			flags["df"] = false;
			flags["of"] = false;

			state = ProcessorState.Sleeping;
		}

		public static void Execute(Instruction instruction)
		{
			if (state == ProcessorState.NotStarted)
			{
				Start();
			}
			byte code = instruction.Opcode;
			switch (code)
			{
				case 0x00:
					Exit();
					break;
				case 0x01:
					Reboot();
					break;
				case 0x02:
					PrintState();
					break;
				case 0x03:
					Mov(instruction.Arg1, instruction.Arg2);
					break;
				case 0x04:
					Add(instruction.Arg1, instruction.Arg2);
					break;
				case 0x05:
					Mul(instruction.Arg1);
					break;
				case 0x06:
					Sub(instruction.Arg1, instruction.Arg2);
					break;
				case 0x07:
					Div(instruction.Arg1);
					break;
				case 0x08:
					Solve();
					break;
				case 0x09:
					Teylor();
					break;
				default:
					break;
			}
		}

		public static void Mov(string dest, string source)
		{
			if (!IsRegister(dest))
			{
				Exit();
				throw new Exception("Wrong operand in mov command");
			}
			Register destReg = registers[dest];
			//add hex numbers
			if (IsRegister(source))
			{
				Register sourceReg = registers[source];
				destReg.Val = sourceReg.Val;
				destReg.Sign = sourceReg.Sign;
				destReg.Exponenta = sourceReg.Exponenta;
				destReg.Mantissa = sourceReg.Mantissa;
				registers[dest] = destReg;
			}
			else
			{
				destReg.Init(float.Parse(source));

				registers[dest] = destReg;
			}
		}
		public static void Add(string dest, string source)
		{
			string op1 = "", op2 = "";
			if (!IsRegister(dest))
			{
				throw new Exception("Bad register name");
			}
			op1 = registers[dest].ToString();

			if (IsRegister(source))
			{
				op2 = registers[source].ToString();
				if (print) Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val + registers[source].Val);

				if (print) Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				if (print) Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val + float.Parse(source));

				if (print) Console.WriteLine("operand2: " + float.Parse(source));
				//check number
			}
			alu.Add(op1, op2, ref flags);

			if (print) Console.WriteLine("\nResult of summation: " + registers[dest] + " (" + registers[dest].Val + ")");
		}
		public static void Sub(string dest, string source)
		{
			string op1 = "", op2 = "";
			if (!IsRegister(dest))
			{
				throw new Exception("Bad register name");
			}

			op1 = registers[dest].ToString();
			if (IsRegister(source))
			{
				op2 = registers[source].ToString();
				if (print) Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val - registers[source].Val);

				if (print) Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				if (print) Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val - float.Parse(source));

				if (print) Console.WriteLine("operand2: " + float.Parse(source));
			}
			alu.Sub(op1, op2, ref flags);
			if (print) Console.WriteLine("\nResult of subtraction: " + registers[dest] + " (" + registers[dest].Val + ")");
		}
		public static void Mul(string source)
		{
			string op1 = "", op2 = "";

			op1 = registers["ax"].ToString();
			if (IsRegister(source))
			{
				op2 = registers[source].ToString();
				if (print) Console.WriteLine("operand1: " + registers["ax"].Val);
				float res = registers["ax"].Val * registers[source].Val;
				if (float.IsInfinity(res)) throw new Exception("Multiplication overflow");
				registers["ax"] = new Register(res);

				if (print) Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				if (print) Console.WriteLine("operand1: " + registers["ax"].Val);
				float res = registers["ax"].Val * float.Parse(source);
				if (float.IsInfinity(res)) throw new Exception("Multiplication overflow");
				registers["ax"] = new Register(res);

				if (print) Console.WriteLine("operand2: " + float.Parse(source));
			}
			alu.Mul(op1, op2, ref flags);
			if (print) Console.WriteLine("\nResult of multiplication: " + registers["ax"] + " (" + registers["ax"].Val + ")");
		}
		public static void Div(string source)
		{
			string op1 = "", op2 = "";

			op1 = registers["ax"].ToString();

			if (IsRegister(source))
			{
				op2 = registers[source].ToString();
				if (print) Console.WriteLine("operand1: " + registers["ax"].Val);
				if (registers[source].Val == 0) throw new Exception("Cannot divide by zero");
				registers["ax"] = new Register(registers["ax"].Val / registers[source].Val);

				if (print) Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				if (print) Console.WriteLine("operand1: " + registers["ax"].Val);
				if (float.Parse(source) == 0) throw new Exception("Cannot divide by zero");
				registers["ax"] = new Register(registers["ax"].Val / float.Parse(source));

				if (print) Console.WriteLine("operand2: " + float.Parse(source));
			}
			alu.Div(op1, op2, ref flags);

			if (print) Console.WriteLine("\nResult of division: " + registers["ax"] + " (" + registers["ax"].Val + ")");
		}
		public static void Solve()
		{
			alu.print = false;
			string a = registers["ax"].ToString();
			string b = registers["bx"].ToString();
			string c = registers["cx"].ToString();
			float a_val = registers["ax"].Val, b_val = registers["bx"].Val, c_val = registers["cx"].Val, x1, x2;
			Console.WriteLine("Solving equation: " + a_val.ToString() + "x^2 + " + b_val.ToString() + "x + " + c_val.ToString() + " = 0");
			if (a_val == 0)
			{
				if (b_val == 0)
				{
					if (c_val == 0) throw new Exception("Infinite number of solutions");
					else throw new Exception("No solutions");
				}
				Mov("ax", "0");
				Sub("ax", "cx");
				Div("bx");
				Console.WriteLine("x1 = x2 = -c / b = " + registers["ax"].Val.ToString());
			}
			else
			{
				float D = b_val * b_val - 4 * a_val * c_val;
				Console.WriteLine("D = " + D.ToString());
				if (D < 0) throw new Exception("Discriminant cannot be less than 0");
				D = (float)Math.Sqrt(D);
				Mov("ax", "0");
				Sub("ax", "bx");
				Mov("cx", "ax");
				Sub("ax", D.ToString());
				Div(a_val.ToString());
				Div("2");
				Mov("bx", "ax");
				Mov("ax", "cx");
				Add("ax", D.ToString());
				Div(a_val.ToString());
				Div("2");
				Console.WriteLine("x1 = " + registers["ax"].Val.ToString() + ", x2 = " + registers["bx"].Val.ToString());
			}
			alu.print = true;
		}
		delegate float del(double x);
		public static void Teylor()
		{
			alu.print = false;
			print = false;
            Console.WriteLine("Solving Teylor decomposition problem for f(x) = -0.5 * ln(1- 2*x*cos(pi / 3) + x^2)");
            string a = registers["ax"].ToString();
			string b = registers["bx"].ToString();
			string h = registers["cx"].ToString();
			string e = registers["dx"].ToString();
			float a_val = registers["ax"].Val, b_val = registers["bx"].Val, h_val = registers["cx"].Val, e_val = registers["dx"].Val;
			Console.WriteLine("Start point: " + a_val.ToString());
			Console.WriteLine("End point: " + b_val.ToString());
			Console.WriteLine("Step value: " + h_val.ToString());
			Console.WriteLine("Error: " + e_val.ToString());
			if (b_val < a_val)
			{
				Console.WriteLine("b cannot be less than a");
				return;
			}
			//del y = (x1) => Convert.ToSingle(Math.Exp(Math.Cos(x1)) * Math.Cos(Math.Sin(x1)));
            del y = (x1) => Convert.ToSingle(-0.5 * Math.Log(1 - (2 * x1 * Math.Cos(Math.PI / 3)) + Math.Pow(x1, 2)));
            for (float x = a_val; x <= b_val; x += h_val)
			{
				Mov("bx", "0");
				int n = 0;
				float yn = y(x), sx = 0;

				while (Math.Abs(yn - sx) >= e_val)
				{
					n++;

                    //Mov("ax", "1");
                    //try
                    //{
                    //    for (int i = 1; i <= n; i++)
                    //    {

                    //        Mul(i.ToString());
                    //    }
                    //}
                    //catch (Exception ex)
                    //{
                    //    Console.WriteLine("Cant't reach error");
                    //    break;
                    //}
                    //Mov("cx", "ax");
                    //Mov("ax", "1");
                    //Mul(n.ToString());
                    //Mul(x.ToString());
                    //Mov("ax", Convert.ToSingle(Math.Cos(registers["ax"].Val)).ToString());
                    //Div("cx");
                    //Add("bx", "ax");

                    try
                    {
                            double temp = (Math.Pow(x, n) * Math.Cos(n * Math.PI / 3)) / n;
                            Add("bx", Convert.ToSingle(temp).ToString());
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine("Cant't reach error");
                        break;
                    }

                    sx = registers["bx"].Val;
				}
				Console.WriteLine("Solution for x = " + x.ToString() + ": Amount of steps = " + n.ToString() 
					+ "; Series value = " + sx.ToString() + "; Function value: " + yn);
			}
			print = true;
			alu.print = true;
		}
		public static bool IsRegister(string val)
		{
			foreach (var r in registers)
			{
				if (r.Key == val)
				{
					return true;
				}
			}
			return false;
		}
		public static void PrintState()
		{
			Console.WriteLine(new string('=', 20));
			Console.WriteLine("Registers: ");
			foreach (var reg in registers)
			{
				if (reg.Value.Val != 0)
				{
					Console.WriteLine(new string('-', 20));
					Console.WriteLine(reg.Key + " = " + reg.Value.Val);
					Console.WriteLine("Sign: " + reg.Value.Sign + " (" +
						(reg.Value.Sign == '1' ? "negative" : "positive") + ")");
					Console.WriteLine("Exponenta: " + reg.Value.Exponenta + " (" +
						reg.Value.GetExp().ToString() + ")");
					Console.WriteLine("Mantissa: " + reg.Value.Mantissa);
				}
				else
				{
					Console.WriteLine(new string('-', 20));
					Console.WriteLine(reg.Key + " = 0.0");
				}
			}
			Console.WriteLine();
			Console.WriteLine("Flags: ");
			foreach (var flag in flags)
			{
				Console.Write(flag.Key + "=" + flag.Value + "; ");
			}
			Console.WriteLine(new string('=', 20));
		}
		public static void Reboot()
		{
			state = ProcessorState.Running;
			registers["ax"] = new Register(0);
			registers["bx"] = new Register(0);
			registers["cx"] = new Register(0);
			registers["dx"] = new Register(0);
			registers["si"] = new Register(0);
			registers["bp"] = new Register(0);
			registers["ip"] = new Register(0);

			flags["cf"] = false;
			flags["pf"] = false;
			flags["af"] = false;
			flags["zf"] = false;
			flags["sf"] = false;
			flags["tf"] = false;
			flags["if"] = false;
			flags["df"] = false;
			flags["of"] = false;
		}
		public static void Exit()
		{
			state = ProcessorState.Stopped;
			registers["ax"] = new Register(0);
			registers["bx"] = new Register(0);
			registers["cx"] = new Register(0);
			registers["dx"] = new Register(0);
			registers["si"] = new Register(0);
			registers["bp"] = new Register(0);
			registers["ip"] = new Register(0);

			flags["cf"] = false;
			flags["pf"] = false;
			flags["af"] = false;
			flags["zf"] = false;
			flags["sf"] = false;
			flags["tf"] = false;
			flags["if"] = false;
			flags["df"] = false;
			flags["of"] = false;
		}
	}
}
