using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop_4_6
{
    public class Instruction
    {
        public string Name { get; set; }
        public string Arg1 { get; set; }
        public string Arg2 { get; set; }

        public Instruction()
        {

        }

        public Instruction(string name)
        {
            Name = name;
        }
    }
}
