using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Plugin;
using System.Windows.Controls;
using System.Windows;

namespace WPFLibrary
{
    public class PluginSource : IPlugin
    {
        public string Activate()
        {
            System.Media.SoundPlayer player = new System.Media.SoundPlayer("Creedence_Clearwater_Revival_-_Fortunate_Son.wav");
            player.Play();

            return "true";
        }

        public void Activate(Image Flashback, Button PluginButton)
        {
            Flashback.Visibility = Visibility.Visible;
            PluginButton.Visibility = Visibility.Visible;
        }
    }
}
