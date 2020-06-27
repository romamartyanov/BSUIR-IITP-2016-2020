using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Emulator
{
	public class BinaryRegister
	{
		public byte Id { get; set; }
		public string H { get; set; }
		public string L { get; set; }
		public BinaryRegister()
		{
			H = new string('0', 8);
			L = new string('0', 8);
			Id = 0x00;
		}
		public BinaryRegister(byte Id)
		{
			H = new string('0', 8);
			L = new string('0', 8);
			this.Id = Id;
		}
		public override string ToString()
		{
			return H + L;
		}
		public string Print(int system)
		{
			switch (system)
			{
				case 2:
					return ToString();
				case 8:
					return Convert.ToInt16(ToString(), 2).ToString("O");
				case 16:
					string hex = Convert.ToString(Convert.ToInt16(ToString(), 2), 16);
					int d = 4 - hex.Length;
					for (int i = 0; i < d; i++)
					{
						hex = "0" + hex;
					}
					return hex;
				case 10:
					return Convert.ToString(Convert.ToInt16(ToString(), 2), 10);
				default:
					throw new Exception("Wrong system");
			}
		}
		public static implicit operator BinaryRegister(string s)
		{
			BinaryRegister r = new BinaryRegister();
			s = Interpreter.Normalize(s, 16);
			r.H = s.Substring(0, 8);
			r.L = s.Substring(8, 8);
			return r;
		}
	}
}
