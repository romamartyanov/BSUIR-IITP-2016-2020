using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace FloatEmulator
{
	public class Register
	{
		public float Val { get; set; }
		public byte Id { get; set; }
		public char Sign { get; set; }
		public string Mantissa { get; set; }
		public string Exponenta { get; set; }
		public Register(float val)
		{
			Init(val);
			Id = 0x00;
		}

		private void Parse(string s)
		{
			Sign = s[0];
			Exponenta = s.Substring(1, 8);
			Mantissa = s.Substring(9, 23);
		}

		public int GetExp() =>
			(Convert.ToInt16(Exponenta, 2) == 0 ? 127 : Convert.ToInt16(Exponenta, 2)) - 127;

		public static int GetExp(string s) => 
			(Convert.ToInt16(s.Substring(1, 8), 2) == 0 ? 127 : Convert.ToInt16(s.Substring(1, 8), 2)) - 127;



		public override string ToString()
		{
			return Sign + Exponenta + Mantissa;
		}
		public string Print()
		{
			return Sign + "|" + Exponenta + "|" + Mantissa;
		}

		public void Init(float val)
		{
			Val = val;
			Sign = val >= 0 ? '0' : '1';
			string s = Sign + Interpreter.Normalize(Interpreter.FloatToBinary(Math.Abs(val)), 31);
			Parse(s);
		}

		public static implicit operator Register(string s)
		{
			Register r = new Register(0);
			r.Sign = s[0];
			r.Exponenta = s.Substring(1, 8);
			r.Mantissa = s.Substring(9, 23);
			return r;
		}
	}
}
