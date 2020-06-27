using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace oop_4_6
{
    public class ALU
    {
        private string working = "";
        private bool overflow = false;
        public string AddInt(string op1, string op2)
        {
            if (working == "")
            {
                Console.WriteLine(op1);
                Console.WriteLine("+");
                Console.WriteLine(op2);
                Console.WriteLine(new string('-', 32));
            }

            int len = op1.Length, rem = 0, cur = 0;
            if (op2[0] == '0') Swap(ref op1, ref op2);
            string res = "";
            for (int i = len - 1; i >= 0; i--)
            {
                cur = Convert.ToInt32(op1[i]) + Convert.ToInt32(op2[i]) - 96 + rem;
                rem = cur / 2;
                res += cur % 2;
                if (cur % 2 == 1 && working == "")
                {
                    Console.WriteLine(Interpreter.Normalize(res, 23));
                }
            }

            if (rem > 0) overflow = true;
            res = new string(res.ToCharArray().Reverse().ToArray());
            if (working == "")
            {
                Console.WriteLine(new string('-', 23));
                Console.WriteLine("Answer: " + Interpreter.Normalize(res, 23));
            }
            return res;
        }

        public string SubInt(string op1, string op2)
        {
            return AddInt(op1, Neg(op2));
        }

        public string Add(string op1, string op2)
        {
            char sgn = '0';
            string res = "";

            int exp1 = Register.GetExp(op1), exp2 = Register.GetExp(op2);
            if (exp1 < exp2 || (exp1 == exp2 &&
                Convert.ToInt32(op1.Substring(9, 23), 2) < Convert.ToInt32(op2.Substring(9, 23), 2)))
            {
                Swap(ref op1, ref op2);
                int t = exp2;
                exp2 = exp1;
                exp1 = t;
            }
            if (exp1 == exp2) overflow = true;
            if (op1[0] == '1') sgn = '1';
            string mant1 = op1.Substring(9, 23), mant2 = op2.Substring(9, 23);
            int diff = exp1 - exp2;
            if (diff > 0)
            {
                mant2 = (new string('0', diff - 1) + "1" + mant2).Substring(0, 23);
            }
            string exp = op1.Substring(1, 8);
            bool wasSub = false;
            Console.WriteLine("\nSumming mantisses: ");
            if (op1[0] == op2[0])
            {
                res = AddInt(mant1, mant2);
            }
            else
            {
                res = SubInt("0" + mant1, "0" + mant2);
                if (res[0] == '1')
                {
                    res = res.Substring(1, 23);
                    for (int i = 0; i < res.Length; i++)
                    {
                        if (res[i] == '1')
                        {
                            Console.WriteLine("\nNormalizing exponent: ");
                            exp = SubInt(exp, Interpreter.Normalize(Convert.ToString(i + 1, 2), 8));
                            res = res.Substring(i + 1, res.Length - i - 1) + new string('0', i + 1);

                            break;
                        }
                    }
                }
                else res = res.Substring(1, 23);
                wasSub = true;
            }

            if (overflow)
            {
                if (op1[0] == op2[0])
                {
                    Console.WriteLine("Normalizing exponent: ");
                    exp = AddInt(exp, Interpreter.Normalize("1", 8));
                }
                if (!wasSub)
                {
                    res = ("0" + res.Substring(0, 22));
                }
            }
            overflow = false;
            res = sgn + exp + res;
           
            Console.WriteLine(res);
            return res;
        }

        public string Sub(string op1, string op2)
        {
            char sgn = '0';
            if (op2[0] == '0') sgn = '1';
            return Add(op1, sgn + op2.Substring(1, op2.Length - 1));
        }

        public string Mul(string op1, string op2)
        {
            char sgn = '0';
            string res = "";

            int exp1 = Register.GetExp(op1), exp2 = Register.GetExp(op2);
            if (op1[0] != op2[0]) sgn = '1';
            string mant1 = op1.Substring(9, 23), mant2 = op2.Substring(9, 23);
            string exp = op1.Substring(1, 8);
            res = MulInt('1' + mant1, '1' + mant2);
            int mod = 1;
            for (int i = 0; i < res.Length; i++)
            {
                if (res[i] == '1')
                {
                    res = res.Substring(i + 1, Math.Min(23, res.Length - i - 1));
                    break;
                }
                mod--;
            }
            exp = Interpreter.Normalize(Convert.ToString(exp1 + exp2 + mod + 127, 2), 8);
            res = sgn + exp + res;
            Console.WriteLine("Resulting mantissa: " + res);
            Console.WriteLine("Resulting exponenta: " + exp);
            return res;
        }

        public string MulInt(string op1, string op2)
        {
            working = "mul";
            Console.WriteLine(op1);
            Console.WriteLine('*');
            Console.WriteLine(op2);
            Console.WriteLine(new string('-', 23));
            string res = Interpreter.Normalize("", 100);
            for (int i = op2.Length - 1; i >= 0; i--)
            {
                if (op2[i] == '1')
                {
                    res = AddInt(res, Interpreter.Normalize(op1 + new string('0', op2.Length - i - 1), 100));
                    Console.WriteLine(Interpreter.Normalize(op1 + new string('0', op2.Length - i - 1), 23));
                }
            }
            Console.WriteLine(new string('-', 23));
            working = "";
            return res.Substring(res.Length - 48, 48);
        }

        public string Div(string op1, string op2)
        {
            char sgn = '0';
            string res = "";

            int exp1 = Register.GetExp(op1), exp2 = Register.GetExp(op2);

            if (op1[0] != op2[0]) sgn = '1';
            string mant1 = op1.Substring(9, 23), mant2 = op2.Substring(9, 23);
            string exp = op1.Substring(1, 8);
            res = DivInt("1" + mant1 + new string('0', 23), "1" + mant2);
            int mod = 1;
            for (int i = 0; i < res.Length; i++)
            {
                if (res[i] == '1')
                {
                    res = res.Substring(i + 1, Math.Min(23, res.Length - i - 1));
                    break;
                }
                mod--;
            }
            exp = Interpreter.Normalize(Convert.ToString(exp1 - exp2 + 127, 2), 8);

            Console.WriteLine("Resulting mantissa: " + res);
            Console.WriteLine("Resulting exponenta: " + exp);
            res = sgn + exp + res;
            return res;
        }

        public string DivInt(string op1, string op2)
        {
            working = "div";
            Console.WriteLine(op1 + "\t|\t" + op2);
            string tmp = "", ans = "", tmpTrimmed = "";
            for (int i = 0; i < op1.Length; i++)
            {
                tmp += op1[i];
                if (Convert.ToInt64(tmp, 2) < Convert.ToInt64(op2, 2))
                {
                    ans += '0';
                }
                else
                {
                    tmpTrimmed = tmp.TrimStart('0');
                    int real_len = tmpTrimmed.Length;
                    Console.Write(new string(' ', i - tmpTrimmed.Length + 1) + op2.TrimStart('0') + '\n');

                    tmp = SubInt(tmp, Interpreter.Normalize(op2, tmp.Length));
                    Console.WriteLine(new string(' ', i - tmpTrimmed.Length + 1) + new string('-', tmpTrimmed.Length));
                    Console.Write(new string(' ', i - tmpTrimmed.Length + 1) + tmp.Substring(tmp.Length - real_len, real_len) + '\n');

                    ans += '1';
                    if (tmp.TrimStart('0') == "") tmp = "";
                }
            }
            tmpTrimmed = tmp.TrimStart('0');
            if (tmpTrimmed == "") tmpTrimmed = "0";
            Console.Write("Remainder: " + tmpTrimmed + '\n');
            Console.WriteLine("Answer: " + ans.TrimStart('0'));
            working = "";
            return ans;
        }

        public string Inc(string s)
        {
            if (working == "") working = "Inc";
            string res = "";
            res = AddInt(s, Interpreter.Normalize("1", s.Length));
            if (working == "Inc") working = "";
            return res;
        }

        private int Abs(string val)
        {
            int x = 0;
            if (IsNeg(val))
            {
                x = 65536 - Convert.ToInt32(val, 2) - 1;
            }
            else x = Convert.ToInt32(val, 2);
            return x;
        }

        private bool IsNeg(string binNum)
        {
            return binNum[0] == '1';
        }

        private void Swap(ref string str1, ref string str2)
        {
            var temp = str2;
            str2 = str1;
            str1 = temp;
        }

        public string Neg(string op1)
        {
            string res = "";
            foreach (char c in op1)
            {
                if (c == '0') res += '1';
                else res += '0';
            }
            return Inc(res);
        }
    }
}
