using Plugin;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace WPF_Material_Design.Forms
{
    /// <summary>
    /// Interaction logic for Plugins.xaml
    /// </summary>
    public partial class Plugins : Window
    {
        List<IPlugin> PluginsList = new List<IPlugin>();


        public Plugins(ref List<IPlugin> _plugins)
        {
            InitializeComponent();

            PluginsList = _plugins;
            foreach (var Plugins in PluginsList)
            {
                TreeViewItem item = new TreeViewItem() { Header = Plugins.ToString() };
                MyTreeView.Items.Add(item);

            }
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                TreeViewItem selectedTVI = (TreeViewItem)MyTreeView.SelectedItem;
                MyTreeView.Items.Remove(selectedTVI);

                foreach (var Plugins in PluginsList.ToList())
                {
                    if (Plugins.ToString().Equals(selectedTVI.Header))
                        PluginsList.Remove(Plugins);
                }
            }
            catch(Exception ex)
            {

            }
            
        }
    }
}
