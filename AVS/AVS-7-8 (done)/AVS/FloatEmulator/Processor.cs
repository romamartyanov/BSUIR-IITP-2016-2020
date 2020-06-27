using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FloatEmulator
{
	public static class Processor
	{
		private static Dictionary<string, Register> registers;
		private static Dictionary<string, bool> flags;
		private static ALU alu;
		private static ProcessorState state = ProcessorState.NotStarted;

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
				Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val + registers[source].Val);
				
				Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val + float.Parse(source));
				
				Console.WriteLine("operand2: " + float.Parse(source));
				//check number
			}
			alu.Add(op1, op2, ref flags);

			Console.WriteLine("\nResult of summation: " + registers[dest] + " (" + registers[dest].Val + ")");
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
				Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val - registers[source].Val);
				
				Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				Console.WriteLine("operand1: " + registers[dest].Val);
				registers[dest] = new Register(registers[dest].Val - float.Parse(source));
				
				Console.WriteLine("operand2: " + float.Parse(source));
			}
			alu.Sub(op1, op2, ref flags);
			Console.WriteLine("\nResult of subtraction: " + registers[dest] + " (" + registers[dest].Val + ")");
		}

		public static void Mul(string source)
		{
			string op1 = "", op2 = "";

			op1 = registers["ax"].ToString();
			if (IsRegister(source))
			{
				op2 = registers[source].ToString();
				Console.WriteLine("operand1: " + registers["ax"].Val);
				float res = registers["ax"].Val * registers[source].Val;
				if (float.IsInfinity(res)) throw new Exception("Multiplication overflow");
				registers["ax"] = new Register(res);
				
				Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				Console.WriteLine("operand1: " + registers["ax"].Val);
				float res = registers["ax"].Val * float.Parse(source);
				registers["ax"] = new Register(res);
				
				Console.WriteLine("operand2: " + float.Parse(source));
			}
			alu.Mul(op1, op2, ref flags);
			Console.WriteLine("\nResult of multiplication: " + registers["ax"] + " (" + registers["ax"].Val + ")");
		}

		public static void Div(string source)
		{
			string op1 = "", op2 = "";

			op1 = registers["ax"].ToString();

			if (IsRegister(source))
			{
				op2 = registers[source].ToString();
				Console.WriteLine("operand1: " + registers["ax"].Val);
				if (registers[source].Val == 0) throw new Exception("Cannot divide by zero");
				registers["ax"] = new Register(registers["ax"].Val / registers[source].Val);
				
				Console.WriteLine("operand2: " + registers[source].Val);
			}
			else
			{
				op2 = new Register(float.Parse(source)).ToString();
				Console.WriteLine("operand1: " + registers["ax"].Val);
				if (float.Parse(source) == 0) throw new Exception("Cannot divide by zero");
				registers["ax"] = new Register(registers["ax"].Val / float.Parse(source));
				
				Console.WriteLine("operand2: " + float.Parse(source));
			}
			alu.Div(op1, op2, ref flags);

			Console.WriteLine("\nResult of division: " + registers["ax"] + " (" + registers["ax"].Val + ")");
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
