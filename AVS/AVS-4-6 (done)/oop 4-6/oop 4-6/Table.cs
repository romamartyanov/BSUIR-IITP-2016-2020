using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop_4_6
{
    public class Table
    {
        private Dictionary<string, byte> registers;
        public Table()
        {
            registers = new Dictionary<string, byte>();
            registers["ax"] = 0x00;
            registers["bx"] = 0x01;
            registers["cx"] = 0x02;
            registers["dx"] = 0x03;
            registers["si"] = 0x04;
            registers["bp"] = 0x05;
            registers["ip"] = 0x06;
        }
    }
}
