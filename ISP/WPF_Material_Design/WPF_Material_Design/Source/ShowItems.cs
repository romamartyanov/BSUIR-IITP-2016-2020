using System;
using System.IO;
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
using System.Windows.Navigation;
using System.Windows.Shapes;
using WPF_Material_Design.Source;
using WPF_Material_Design.Forms;
using System.Runtime.Serialization.Formatters.Binary;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace WPF_Material_Design.Source
{
    static public class ShowItems
    {
        static public void ShowConstellations(ref TreeView MainTreeView,
            ref List<Constellations> Constellations,
            ref List<Stars> Stars,
            ref List<NGCObjects> NGCObjects,
            ref List<Planets> Planets,
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (Constellations constellation in Constellations)
            {
                TreeViewItem constellation_item = new TreeViewItem() { Name = constellation.ID, Header = constellation.Name };
                MainTreeView.Items.Add(constellation_item);
                constellation_item.IsExpanded = true;

                foreach (Stars star in Stars)
                {
                    if (star.Constellatoin == constellation.Name)
                    {
                        TreeViewItem star_item = new TreeViewItem() { Name = star.ID, Header = star.Name };
                        constellation_item.Items.Add(star_item);
                        star_item.IsExpanded = true;

                        foreach (Planets planet in Planets)
                        {

                            if (planet.Center_body == star.Name)
                            {
                                TreeViewItem planet_item = new TreeViewItem() { Name = planet.ID, Header = planet.Name };
                                star_item.Items.Add(planet_item);
                                planet_item.IsExpanded = true;
                            }
                        }
                    }
                }

                foreach (NGCObjects ngc in NGCObjects)
                {
                    if (ngc.Constellatoin == constellation.Name)
                    {
                        TreeViewItem ngc_item = new TreeViewItem() { Name = ngc.ID, Header = ngc.Name };
                        constellation_item.Items.Add(ngc_item);
                        ngc_item.IsExpanded = true;
                    }
                }
            }
        }


        static public void ShowConstellations(ref TreeView MainTreeView,
            ref IEnumerable<Constellations> Constellations,
            ref List<Stars> Stars,
            ref List<NGCObjects> NGCObjects,
            ref List<Planets> Planets,
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (Constellations constellation in Constellations)
            {
                TreeViewItem constellation_item = new TreeViewItem() { Name = constellation.ID, Header = constellation.Name };
                MainTreeView.Items.Add(constellation_item);
                constellation_item.IsExpanded = true;

                foreach (Stars star in Stars)
                {
                    if (star.Constellatoin == constellation.Name)
                    {
                        TreeViewItem star_item = new TreeViewItem() { Name = star.ID, Header = star.Name };
                        constellation_item.Items.Add(star_item);
                        star_item.IsExpanded = true;

                        foreach (Planets planet in Planets)
                        {

                            if (planet.Center_body == star.Name)
                            {
                                TreeViewItem planet_item = new TreeViewItem() { Name = planet.ID, Header = planet.Name };
                                star_item.Items.Add(planet_item);
                                planet_item.IsExpanded = true;
                            }
                        }
                    }
                }

                foreach (NGCObjects ngc in NGCObjects)
                {
                    if (ngc.Constellatoin == constellation.Name)
                    {
                        TreeViewItem ngc_item = new TreeViewItem() { Name = ngc.ID, Header = ngc.Name };
                        constellation_item.Items.Add(ngc_item);
                        ngc_item.IsExpanded = true;
                    }
                }
            }
        }


        static public void ShowStars(ref TreeView MainTreeView, 
            ref List<Stars> Stars,
            ref List<Planets> Planets,
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (Stars star in Stars)
            {
                TreeViewItem star_item = new TreeViewItem() { Name = star.ID, Header = star.Name };
                MainTreeView.Items.Add(star_item);
                star_item.IsExpanded = true;

                foreach (Planets planet in Planets)
                {

                    if (planet.Center_body == star.Name)
                    {
                        TreeViewItem planet_item = new TreeViewItem() { Name = planet.ID, Header = planet.Name };
                        star_item.Items.Add(planet_item);
                        planet_item.IsExpanded = true;
                    }
                }
            }
        }


        static public void ShowStars(ref TreeView MainTreeView,
            ref IEnumerable<Stars> Stars,
            ref List<Planets> Planets,
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (Stars star in Stars)
            {
                TreeViewItem star_item = new TreeViewItem() { Name = star.ID, Header = star.Name };
                MainTreeView.Items.Add(star_item);
                star_item.IsExpanded = true;

                foreach (Planets planet in Planets)
                {

                    if (planet.Center_body == star.Name)
                    {
                        TreeViewItem planet_item = new TreeViewItem() { Name = planet.ID, Header = planet.Name };
                        star_item.Items.Add(planet_item);
                        planet_item.IsExpanded = true;
                    }
                }
            }
        }


        static public void ShowNGCObjects(ref TreeView MainTreeView, 
            ref List<NGCObjects> NGCObjects, 
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (NGCObjects ngc in NGCObjects)
            {
                TreeViewItem ngc_item = new TreeViewItem() { Name = ngc.ID, Header = ngc.Name };
                MainTreeView.Items.Add(ngc_item);
                ngc_item.IsExpanded = true;
            }
        }

        static public void ShowNGCObjects(ref TreeView MainTreeView,
            ref IEnumerable<NGCObjects> NGCObjects,
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (NGCObjects ngc in NGCObjects)
            {
                TreeViewItem ngc_item = new TreeViewItem() { Name = ngc.ID, Header = ngc.Name };
                MainTreeView.Items.Add(ngc_item);
                ngc_item.IsExpanded = true;
            }
        }


        static public void ShowPlanets(ref TreeView MainTreeView, 
            ref List<Planets> Planets, 
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (Planets planet in Planets)
            {
                TreeViewItem planet_item = new TreeViewItem() { Name = planet.ID, Header = planet.Name };
                MainTreeView.Items.Add(planet_item);
                planet_item.IsExpanded = true;
            }
        }

        static public void ShowPlanets(ref TreeView MainTreeView,
            ref IEnumerable<Planets> Planets,
            Dictionary<string, string> TreeVievFlag)
        {
            MainTreeView.Items.Clear();

            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);

            foreach (Planets planet in Planets)
            {
                TreeViewItem planet_item = new TreeViewItem() { Name = planet.ID, Header = planet.Name };
                MainTreeView.Items.Add(planet_item);
                planet_item.IsExpanded = true;
            }
        }
    }
}
