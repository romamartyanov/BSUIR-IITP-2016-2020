using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Emulator
{
	public class Program
	{
		static void Main(string[] args)
		{
			string command;
			Console.WriteLine("\t\t\t\t\tALU Emulator, Roman Martyanov");
            while (true)
			{
				Console.Write("$");
				command = Console.ReadLine();
				if (command == "0") break;
				try
				{
					Instruction instruction = Interpreter.Parse(command);
					Processor.Execute(instruction);
				}
				catch (Exception e)
				{
					Console.WriteLine(e.Message);
					//break;
				}
				if (Processor.State == ProcessorState.Stopped)
				{
					break;
				}
			}
		}
	}
}
