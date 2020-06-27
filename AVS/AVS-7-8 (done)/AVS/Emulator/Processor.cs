using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Emulator
{
	public static class Processor
	{
		private static Dictionary<string, BinaryRegister> registers;
		private static Dictionary<string, bool> flags;
		//private static Dictionary<string, string> lRegisters;
		private static Dictionary<string, string> smallRegisters;
		private static ALU alu;
		private static ProcessorState state = ProcessorState.NotStarted;
		private const int maxBigNum = 32767;
		private const int maxSmallNum = 127;

		public static Dictionary<string, BinaryRegister> Registers { get => registers; }
		public static Dictionary<string, bool> Flags { get => flags; }
		public static ProcessorState State => state;

		public static void Start()
		{
			registers = new Dictionary<string, BinaryRegister>();
			flags = new Dictionary<string, bool>();
			alu = new ALU();
			//lRegisters = new Dictionary<string, string>();
			smallRegisters = new Dictionary<string, string>();
			registers["ax"] = new BinaryRegister(0x01);
			registers["bx"] = new BinaryRegister(0x02);
			registers["cx"] = new BinaryRegister(0x03);
			registers["dx"] = new BinaryRegister(0x04);
			registers["si"] = new BinaryRegister(0x05);
			registers["bp"] = new BinaryRegister(0x06);
			registers["ip"] = new BinaryRegister(0x07);

			flags["cf"] = false;
			flags["pf"] = false;
			flags["af"] = false;
			flags["zf"] = false;
			flags["sf"] = false;
			flags["tf"] = false;
			flags["if"] = false;
			flags["df"] = false;
			flags["of"] = false;

			smallRegisters["al"] = "ax";
			smallRegisters["bl"] = "bx";
			smallRegisters["cl"] = "cx";
			smallRegisters["dl"] = "dx";

			smallRegisters["ah"] = "ax";
			smallRegisters["bh"] = "bx";
			smallRegisters["ch"] = "cx";
			smallRegisters["dh"] = "dx";
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
			if (!IsBigRegister(dest))
			{
				if (IsBigRegister(source))
				{
					Exit();
					throw new Exception("Wrong operand in mov command");
				}
				if (IsSmallRegister(dest))
				{
					BinaryRegister destSmallBinReg = registers[smallRegisters[dest]];
					if (IsSmallRegister(source))
					{
						if (dest[1] == 'l' && source[1] == 'l')
						{
							destSmallBinReg.L = registers[smallRegisters[source]].L;
						}
						else if (dest[1] == 'l' && source[1] == 'h')
						{
							destSmallBinReg.L = registers[smallRegisters[source]].H;
						}
						else if (dest[1] == 'h' && source[1] == 'l')
						{
							destSmallBinReg.H = registers[smallRegisters[source]].L;
						}
						else if (dest[1] == 'h' && source[1] == 'h')
						{
							destSmallBinReg.H = registers[smallRegisters[source]].H;
						}
					}
					//if number -- add check for a number
					else
					{
						if (Int32.Parse(source) > maxSmallNum)
						{
							throw new Exception("Constant too large");
						}
						if (dest[1] == 'l')
						{
							destSmallBinReg.L = Interpreter.Normalize(Convert.ToString(Int32.Parse(source), 2), 8);
						}
						else
						{
							destSmallBinReg.H = Interpreter.Normalize(Convert.ToString(Int32.Parse(source), 2), 8);
						}
					}
				}
				else
				{
					Exit();
					throw new Exception("Wrong operand in mov command");
				}
				return;
			}
			BinaryRegister destReg = registers[dest];
			//add hex numbers
			if (IsBigRegister(source))
			{
				BinaryRegister sourceReg = registers[source];
				destReg.H = sourceReg.H;
				destReg.L = sourceReg.L;
				registers[dest] = destReg;
			}
			else
			{
				int val = Int32.Parse(source);
				if (val > maxBigNum)
				{
					throw new Exception("Constant too large");
				}
				string binSource = Interpreter.Normalize(Convert.ToString(Int32.Parse(source), 2), 16);
				destReg.H = binSource.Substring(0, 8);
				destReg.L = binSource.Substring(8, 8);
				registers[dest] = destReg;
			}
		}

		public static void Add(string dest, string source)
		{
			string op1 = "", op2 = "";
			if (IsBigRegister(dest))
			{
				op1 = registers[dest].ToString();
				if (IsSmallRegister(source))
				{
					throw new Exception("Operand types do not match");
				}
				if (IsBigRegister(source))
				{
					op2 = registers[source].ToString();
				}
				else
				{
					op2 = Interpreter.Normalize(Convert.ToString(Convert.ToInt32(source), 2), 16);
					//check number

				}
				registers[dest] = alu.Add(op1, op2, ref flags);
			}
			else if (IsSmallRegister(dest))
			{
				BinaryRegister smallReg = registers[smallRegisters[dest]];
				string d = "l";
				if (IsBigRegister(source))
				{

					throw new Exception("Operand types do not match");
				}
				if (dest[1] == 'l')
				{
					op1 = registers[smallRegisters[dest]].L;
				}
				else
				{
					op1 = registers[smallRegisters[dest]].H;
					d = "h";
				}
				if (IsSmallRegister(source))
				{
					if (source[1] == 'l')
					{
						op2 = registers[smallRegisters[source]].L;
					}
					else
					{
						op2 = registers[smallRegisters[source]].H;
					}
				}
				else
				{
					op2 = Convert.ToString(Convert.ToInt32(source), 2);
					op2 = op2.Substring(op2.Length - 8, 8);
				}
				if (d == "l")
				{
					smallReg.L = alu.Add(op1, op2, ref flags);
				}
				else
				{
					smallReg.H = alu.Add(op1, op2, ref flags);
				}
			}
		}

		public static void Sub(string dest, string source)
		{
			string op1 = "", op2 = "";
			if (IsBigRegister(dest))
			{
				op1 = registers[dest].ToString();
				if (IsSmallRegister(source))
				{
					throw new Exception("Operand types do not match");
				}
				if (IsBigRegister(source))
				{
					op2 = registers[source].ToString();
				}
				else
				{
					op2 = Interpreter.Normalize(Convert.ToString(Convert.ToInt32(source), 2), 16);
					//check number

				}
				registers[dest] = alu.Sub(op1, op2, ref flags);
			}
			else if (IsSmallRegister(dest))
			{
				BinaryRegister smallReg = registers[smallRegisters[dest]];
				string d = "l";
				if (IsBigRegister(source))
				{

					throw new Exception("Operand types do not match");
				}
				if (dest[1] == 'l')
				{
					op1 = registers[smallRegisters[dest]].L;
				}
				else
				{
					op1 = registers[smallRegisters[dest]].H;
					d = "h";
				}
				if (IsSmallRegister(source))
				{
					if (source[1] == 'l')
					{
						op2 = registers[smallRegisters[source]].L;
					}
					else
					{
						op2 = registers[smallRegisters[source]].H;
					}
				}
				else
				{
					op2 = Convert.ToString(Convert.ToInt32(source), 2);
					op2 = op2.Substring(op2.Length - 8, 8);
				}
				if (d == "l")
				{
					smallReg.L = alu.Sub(op1, op2, ref flags);
				}
				else
				{
					smallReg.H = alu.Sub(op1, op2, ref flags);
				}
			}
		}

		public static void Mul(string source)
		{
			string op1 = "", op2 = "";

			op1 = registers["ax"].ToString();
			if (IsSmallRegister(source))
			{
				if (source[1] == 'l') op2 = Interpreter.Normalize(registers[smallRegisters[source]].L, 16);
				else op2 = Interpreter.Normalize(registers[smallRegisters[source]].H, 16);
			}
			else if (IsBigRegister(source))
			{
				op2 = registers[source].ToString();
			}
			else
			{
				op2 = Interpreter.Normalize(Convert.ToString(Convert.ToInt32(source), 2), 16);
			}
			registers["ax"] = alu.Mul(op1, op2, ref flags);


			Console.WriteLine(registers["ax"]);
		}

		public static void Div(string source)
		{
			string op1 = "", op2 = "";

			op1 = registers["ax"].ToString();
			if (IsSmallRegister(source))
			{
				if (source[1] == 'l') op2 = Interpreter.Normalize(registers[smallRegisters[source]].L, 16);
				else op2 = Interpreter.Normalize(registers[smallRegisters[source]].H, 16);
			}
			else if (IsBigRegister(source))
			{
				op2 = registers[source].ToString();
			}
			else
			{
				op2 = Interpreter.Normalize(Convert.ToString(Convert.ToInt32(source), 2), 16);
			}
			registers["ax"] = alu.Div(op1, op2, ref flags);

			Console.WriteLine(registers["ax"]);
		}

		public static bool IsBigRegister(string val)
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

		public static bool IsSmallRegister(string val)
		{
			return smallRegisters.Keys.Contains(val);
		}

		public static void PrintState()
		{
			Console.WriteLine(new string('=', 20));
			Console.Write("Registers: ");
			foreach (var reg in registers)
			{
				Console.Write(reg.Key + "=" + reg.Value.Print(16) + "; ");
			}
			Console.WriteLine();
			Console.WriteLine("Flags: ");
			foreach (var flag in flags)
			{
				Console.Write(flag.Key + "=" + flag.Value + "; ");
			}
			Console.WriteLine("\n" + new string('=', 20));
		}

		private static bool CheckBig(string num)
		{
			return Convert.ToInt32(num) > 65535;
		}

		public static int MaxBig => maxBigNum;

		private static bool CheckSmall(string num)
		{
			return Convert.ToInt32(num) > 255;
		}

		public static void Reboot()
		{
			state = ProcessorState.Running;
			registers["ax"] = new BinaryRegister(0x01);
			registers["bx"] = new BinaryRegister(0x02);
			registers["cx"] = new BinaryRegister(0x03);
			registers["dx"] = new BinaryRegister(0x04);
			registers["si"] = new BinaryRegister(0x05);
			registers["bp"] = new BinaryRegister(0x06);
			registers["ip"] = new BinaryRegister(0x07);

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
			registers["ax"] = new BinaryRegister(0x01);
			registers["bx"] = new BinaryRegister(0x02);
			registers["cx"] = new BinaryRegister(0x03);
			registers["dx"] = new BinaryRegister(0x04);
			registers["si"] = new BinaryRegister(0x05);
			registers["bp"] = new BinaryRegister(0x06);
			registers["ip"] = new BinaryRegister(0x07);

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
