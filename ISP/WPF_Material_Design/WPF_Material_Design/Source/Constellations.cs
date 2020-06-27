using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WPF_Material_Design.Source
{
    [Serializable]
    public class Constellations
    {
        public string Name { get; set; }

        public string ID { get; set; }
        //public virtual string Pic_Url { get; set; }

        public string Declination_from { get; set; }
        public string Declination_to { get; set; }
        public string Right_Ascension_from { get; set; }
        public string Right_Ascension_to { get; set; }
        public string Info { get; set; }


        public Constellations()
        {
            Name = null;
            //Pic_Url = null;

            Right_Ascension_from = null;
            Right_Ascension_to = null;

            Declination_from = null;
            Declination_to = null;
            Info = null;
        }

        public void Create(string name,
                            string declination_from,
                            string declination_to,

                            string right_Ascension_from,
                            string right_Ascension_to,
                            string info)
        {
            this.Name = name;

            //this.Pic_Url = Console.ReadLine();

            this.Declination_from = declination_from;
            this.Declination_to = declination_to;

            this.Right_Ascension_from = right_Ascension_from;
            this.Right_Ascension_to = right_Ascension_to;
            this.Info = info;

            this.ID = "Constellations_" + this.Name.Replace(" ", "_").Replace("-", "_");
        }
    }
}
