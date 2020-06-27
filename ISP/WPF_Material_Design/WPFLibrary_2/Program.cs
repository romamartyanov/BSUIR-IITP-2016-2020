using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;

namespace WPFLibrary_2
{
    class Program
    {
        static void Main(string[] args)
        {
        }

        
    }

    public interface IPlugin
    {
        void Activate(Image image, Button button);
    }
}
