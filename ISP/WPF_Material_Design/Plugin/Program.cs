using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;

namespace Plugin
{
    class Program
    {
        static void Main(string[] args)
        {
        }
    }

    public interface IPlugin
    {
        string Activate();
        void Activate(Image Flashback, Button PluginButton);
    }
}