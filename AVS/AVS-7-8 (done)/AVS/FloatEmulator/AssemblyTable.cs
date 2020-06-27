using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FloatEmulator
{
	public class AssemblyTable
	{
		private Dictionary<string, byte> registers;
		private Dictionary<string, byte> flags;
		private Dictionary<string, byte> instructions;
		public AssemblyTable()
		{
			registers = new Dictionary<string, byte>();
			flags = new Dictionary<string, byte>();
			instructions = new Dictionary<string, byte>();
			Init();
		}

		private void Init()
		{
			registers["ax"] = 0x00;
			registers["bx"] = 0x01;
			registers["cx"] = 0x02;
			registers["dx"] = 0x03;
			registers["si"] = 0x04;
			registers["bp"] = 0x05;
			registers["ip"] = 0x06;

			flags["cf"] = 0x00;
			flags["pf"] = 0x02;
			flags["af"] = 0x04;
			flags["zf"] = 0x06;
			flags["sf"] = 0x07;
			flags["tf"] = 0x08;
			flags["if"] = 0x09;
			flags["df"] = 0x0A;
			flags["of"] = 0x0B;

			instructions["stop"] = 0x00;
			instructions["reboot"] = 0x01;
			instructions["state"] = 0x02;
			instructions["mov"] = 0x03;
			instructions["add"] = 0x04;
			instructions["mul"] = 0x05;
			instructions["sub"] = 0x06;
			instructions["div"] = 0x07;
		}
		public string GetInstruction(byte code)
		{
			foreach (var instruction in instructions)
			{
				if (instruction.Value == code)
				{
					return instruction.Key;
				}
			}
			return "";
		}
		public byte GetInstructionCode(string instruction)
		{
			//!!
			return instructions[instruction];
		}
	}
}
