using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using WPFLibrary_2;

namespace Plugin_2
{
    public class Class1 : IPlugin
    {
        public void Activate(Image Flashback, Button PluginButton)
        {
            Flashback.Visibility = Visibility.Visible;
            PluginButton.Visibility = Visibility.Visible;
        }
    }
}
