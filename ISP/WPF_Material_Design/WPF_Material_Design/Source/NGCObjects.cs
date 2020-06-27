using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WPF_Material_Design.Source
{
    [Serializable]
    public class NGCObjects
    {
        public string Name { get; set; }
        public string ID { get; set; }
        public string Constellatoin { get; set; }

        //public virtual string Pic_Url { get; set; }

        public string Declination { get; set; }
        public string Right_Ascension { get; set; }

        public decimal? Apparent_Star_Magnitude { get; set; }
        public decimal? Redshift { get; set; }

        public ulong? Distance { get; set; }

        public string Type { get; set; }
        public string Info { get; set; }


        public NGCObjects()
        {
            Name = null;
            Constellatoin = null;

            Declination = null;
            Right_Ascension = null;

            Apparent_Star_Magnitude = null;
            Redshift = null;
            Distance = null;

            Type = null;
            Info = null;
        }

        
        public void Create(string name,
                            string constellatoin,
                            string declination,
                            string right_Ascension,

                            decimal? apparent_Star_Magnitude,
                            decimal? redshift,
                            ulong? distance,

                            string type,
                            string info)
        {
            this.Name = name;

            //this.Pic_Url = Console.ReadLine();

            this.Constellatoin = constellatoin;
            this.Declination = declination;

            this.Right_Ascension = right_Ascension;
            this.Apparent_Star_Magnitude = apparent_Star_Magnitude;
            this.Redshift = redshift;
            this.Distance = distance;

            this.Type = type;
            this.Info = info;



            this.ID = "NGCObjects_" + this.Name.Replace(" ","_").Replace("-","_");
        }

    }
}
