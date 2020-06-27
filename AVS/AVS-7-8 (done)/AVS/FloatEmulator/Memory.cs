using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FloatEmulator
{
	public static class Memory
	{
		private static byte[] mem = new byte[maxCapacity];
		private const int maxCapacity = 65536;


		public static void Reset()
		{
			for (int i = 0; i < maxCapacity; i++)
			{
				mem[i] = 0;
			}
		}

		public static byte Load(byte segment, byte address)
		{
			int addr = (int)segment * 256 + address;
			if (addr < 0 || addr >= maxCapacity)
			{
				throw new Exception("Can't acccess memmory");
			}
			return mem[addr];
		}

		public static void SetByte(byte segment, byte address, byte val)
		{
			int addr = (int)segment * 256 + address;
			if (addr < 0 || addr >= maxCapacity)
			{
				throw new Exception("Can't acccess memmory");
			}
			mem[addr] = val;
		}

		public static void Print()
		{
			for (int i = 0; i < 256; i++)
			{
				string s = "";
				for (int j = 0; j < 256; j++)
				{
					s += mem[i * 256 + j].ToString() + " ";
				}
				Console.WriteLine(s);
			}
		}
	}
}
