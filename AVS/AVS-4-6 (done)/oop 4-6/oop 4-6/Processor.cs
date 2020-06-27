using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop_4_6
{
    public class Processor
    {
        private static Dictionary<string, Register> registers;
        private static ALU alu;
        public static Dictionary<string, Register> Registers { get => registers; }
        public Processor()
        {
            registers = new Dictionary<string, Register>();
            alu = new ALU();
            registers["ax"] = new Register(0);
            registers["bx"] = new Register(0);
            registers["cx"] = new Register(0);
            registers["dx"] = new Register(0);
            registers["si"] = new Register(0);
            registers["bp"] = new Register(0);
            registers["ip"] = new Register(0);
        }
       
        public void Run(Instruction instruction)
        {
           
            string name = instruction.Name;
            switch (name)
            {
                case "stop":
                    Exit();
                    break;
                case "reboot":
                    Reboot();
                    break;
                case "state":
                    PrintState();
                    break;
                case "mov":
                    Mov(instruction.Arg1, instruction.Arg2);
                    break;
                case "add":
                    Add(instruction.Arg1, instruction.Arg2);
                    break;
                case "mul":
                    Mul(instruction.Arg1);
                    break;
                case "sub":
                    Sub(instruction.Arg1, instruction.Arg2);
                    break;
                case "div":
                    Div(instruction.Arg1);
                    break;
                default:
                    Console.WriteLine("Bad input. Try again");
                    break;
            }
        }

        public static void Mov(string dest, string source)
        {
            if (!IsRegister(dest))
            {
                Exit();
                throw new Exception("Wrong operand in mov command");
            }
            Register destReg = registers[dest];
            if (IsRegister(source))
            {
                Register sourceReg = registers[source];
                destReg.Val = sourceReg.Val;
                destReg.Sign = sourceReg.Sign;
                destReg.Exponenta = sourceReg.Exponenta;
                destReg.Mantissa = sourceReg.Mantissa;
                registers[dest] = destReg;
            }
            else
            {
                destReg.Init(float.Parse(source));

                registers[dest] = destReg;
            }
        }

        public static void Add(string dest, string source)
        {
            string op1 = "", op2 = "";
            if (!IsRegister(dest))
            {
                throw new Exception("Bad register name");
            }
            op1 = registers[dest].ToString();

            if (IsRegister(source))
            {
                op2 = registers[source].ToString();
                float res = registers["ax"].Val + registers[source].Val;
                if (float.IsInfinity(res)) throw new Exception("adding overflow");
                registers[dest] = new Register(registers[dest].Val + registers[source].Val);
            }
            else
            {
                op2 = new Register(float.Parse(source)).ToString();
                float res = registers["ax"].Val + float.Parse(source);
                if (float.IsInfinity(res)) throw new Exception("adding overflow");
                registers[dest] = new Register(registers[dest].Val + float.Parse(source));
            }
            alu.Add(op1, op2);

            Console.WriteLine("\nResult: " + registers[dest] + " (" + registers[dest].Val + ")");
        }

        public static void Sub(string dest, string source)
        {
            string op1 = "", op2 = "";
            if (!IsRegister(dest))
            {
                throw new Exception("Bad register name");
            }

            op1 = registers[dest].ToString();
            if (IsRegister(source))
            {
                op2 = registers[source].ToString();
                registers[dest] = new Register(registers[dest].Val - registers[source].Val);
            }
            else
            {
                op2 = new Register(float.Parse(source)).ToString();
                registers[dest] = new Register(registers[dest].Val - float.Parse(source));
            }
            alu.Sub(op1, op2);
            Console.WriteLine("\nResult: " + registers[dest] + " (" + registers[dest].Val + ")");
        }

        public static void Mul(string source)
        {
            string op1 = "", op2 = "";

            op1 = registers["ax"].ToString();
            if (IsRegister(source))
            {
                op2 = registers[source].ToString();
                float res = registers["ax"].Val * registers[source].Val;
                if (float.IsInfinity(res)) throw new Exception("multiplication overflow");
                registers["ax"] = new Register(registers["ax"].Val * registers[source].Val);
            }
            else
            {
                op2 = new Register(float.Parse(source)).ToString();
                Console.WriteLine("operand1: " + registers["ax"].Val);
                float res = registers["ax"].Val * float.Parse(source);
                if (float.IsInfinity(res)) throw new Exception("multiplication overflow");
                registers["ax"] = new Register(registers["ax"].Val * float.Parse(source));

                Console.WriteLine("operand2: " + float.Parse(source));
            }
            alu.Mul(op1, op2);
            Console.WriteLine("\nResult: " + registers["ax"] + " (" + registers["ax"].Val + ")");
        }

        public static void Div(string source)
        {
            string op1 = "", op2 = "";

            op1 = registers["ax"].ToString();

            if (IsRegister(source))
            {
                op2 = registers[source].ToString();
                if (registers[source].Val == 0) throw new Exception("Cannot divide by zero");
                registers["ax"] = new Register(registers["ax"].Val / registers[source].Val);
            }
            else
            {
                op2 = new Register(float.Parse(source)).ToString();
                registers["ax"] = new Register(registers["ax"].Val / float.Parse(source));
            }
            alu.Div(op1, op2);

            Console.WriteLine("\nResult: " + registers["ax"] + " (" + registers["ax"].Val + ")");
        }

        public static bool IsRegister(string val)
        {
            foreach (var r in registers)
            {
                if (r.Key == val)
                {
                    return true;
                }
            }
            return false;
        }

        public static void PrintState()
        {
            Console.WriteLine(new string('=', 20));
            Console.WriteLine("Registers: ");
            foreach (var reg in registers)
            {
                if (reg.Value.Val != 0)
                {
                    Console.WriteLine(new string('-', 20));
                    Console.WriteLine(reg.Key + " = " + reg.Value.Val);
                    Console.WriteLine("Sign: " + reg.Value.Sign);// + " (" +
                    Console.WriteLine("Exponenta: " + reg.Value.Exponenta + " (" +
                        reg.Value.GetExp().ToString() + ")");
                    Console.WriteLine("Mantissa: " + reg.Value.Mantissa);
                }
                else
                {
                    Console.Write(reg.Key + " = 0.0" + " ");
                }
            }
            Console.WriteLine();
           
           
            Console.WriteLine(new string('=', 20));
        }

        public static void Reboot()
        {
            registers["ax"] = new Register(0);
            registers["bx"] = new Register(0);
            registers["cx"] = new Register(0);
            registers["dx"] = new Register(0);
            registers["si"] = new Register(0);
            registers["bp"] = new Register(0);
            registers["ip"] = new Register(0);

        }

        public static void Exit()
        {
            registers["ax"] = new Register(0);
            registers["bx"] = new Register(0);
            registers["cx"] = new Register(0);
            registers["dx"] = new Register(0);
            registers["si"] = new Register(0);
            registers["bp"] = new Register(0);
            registers["ip"] = new Register(0);

          
        }
    }
}
