using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop_4_6
{
    class Program
    {
        static void Main(string[] args)
        {
            string command;
            Console.WriteLine("\t\t\t\t\tALU Emulator, Roman Martyanov");
            Processor a = new Processor();


            while (true)
            {
                Console.WriteLine("$");

                command = Console.ReadLine();
                try
                {
                    Instruction instruction = Interpreter.Parse(command);
                    a.Run(instruction);

                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }

            }

        }
    }
}
