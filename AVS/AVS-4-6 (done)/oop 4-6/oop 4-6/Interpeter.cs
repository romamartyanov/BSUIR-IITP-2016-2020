using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop_4_6
{
    static class Interpreter
    {
        private static Table assemblyTable = new Table();

        public static Instruction Parse(string command)
        {
            string[] args = System.Text.RegularExpressions.Regex.Split(command, @"\s{1,}"); ;
            if (args.Length > 3)
            {
                throw new Exception("Wrong command");
            }
            Instruction instruction = new Instruction()
            {
                Name = args[0],
            };
            if (args.Length == 1)
            {
                return instruction;
            }
            instruction.Arg1 = args[1];
            if (args.Length == 2)
            {
                return instruction;
            }
            instruction.Arg2 = args[2];
            return instruction;
        }

        private static string Prepare(string command)
        {
            command = command.Trim().ToLower().Replace(',', ' ');
            return command;
        }

        public static string FloatToBinary(float number)
        {
            int dec = BitConverter.ToInt32(BitConverter.GetBytes(number), 0);

            return Convert.ToString(dec, 2);
        }

        public static string Normalize(string bin, int len)
        {
            if (bin.Length > len)
            {
                bin = bin.Substring(bin.Length - len, len);
            }
            int d = len - bin.Length;
            for (int i = 0; i < d; i++)
            {
                bin = "0" + bin;
            }
            return bin;
        }
    }
}
