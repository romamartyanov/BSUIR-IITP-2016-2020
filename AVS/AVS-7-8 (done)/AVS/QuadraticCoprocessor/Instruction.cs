using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuadraticCoprocessor
{
	public class Instruction
	{
		public string Name { get; set; }
		public byte Opcode { get; set; }
		public string Arg1 { get; set; }
		public string Arg2 { get; set; }
		public InstructionType InstructionType { get; set; }

		public Instruction()
		{
			InstructionType = InstructionType.Double;
		}

		public Instruction(string name)
		{
			Name = name; 
			InstructionType = InstructionType.Double;
		}

		public void TransformName()
		{
			switch (Name)
			{
				case "exit":
					Opcode = 0x00;
					break;
				case "reboot":
					Opcode = 0x01;
					break;
				case "state":
					Opcode = 0x02;
					break;
				case "mov":
					Opcode = 0x03;
					break;
				case "add":
					Opcode = 0x04;
					break;
				default:
					Opcode = 0xFF;
					break;
			}
		} 
	}
}
