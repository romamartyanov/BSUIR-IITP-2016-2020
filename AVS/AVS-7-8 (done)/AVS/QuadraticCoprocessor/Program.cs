using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuadraticCoprocessor
{
	public class Program
	{
		static void Main(string[] args)
		{
			string command;
			
			Console.WriteLine("\t\t\t\tQuadratic coproecssor. Roman Martyanov");

            while (true)
			{
				Console.Write("$");
				command = Console.ReadLine();
				if (command == "0")
                    break;
				try
				{
					Instruction instruction = Interpreter.Parse(command);
					Processor.Execute(instruction);
				}
				catch (Exception e)
				{
					string mes = e.Message;
					if (mes.Contains("Single")) mes = mes.Replace("Single", "float");
					Console.WriteLine(mes);
					//break;
				}
				if (Processor.State == ProcessorState.Stopped)
				{
					break;
				}
			}

            Console.ReadLine();
        }
	}
}
