using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;

using System.Runtime.Serialization.Formatters.Binary;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;


namespace WPF_Material_Design.Source
{
    static public class SerializingCollections
    {
        //static string SolutionPath = @"E:\University\Laboratory works\CSharp\WPF_labs\WPF_Material_Design\WPF_Material_Design\";
        static string SolutionPath = "";


        static public void ConstellationCollectionJSONSerialization(List<Constellations> Constellations, string path)
        {
            string jsonWithConverter = JsonConvert.SerializeObject(Constellations, new StringEnumConverter());
            File.WriteAllText(SolutionPath + $"{path}", jsonWithConverter);
        }


        static public void StarsCollectionJSONSerialization(List<Stars> Stars, string path)
        {
            string jsonWithConverter = JsonConvert.SerializeObject(Stars, new StringEnumConverter());
            File.WriteAllText(SolutionPath + $@"{path}" , jsonWithConverter);
        }


        static public void PlanetsCollectionJSONSerialization(List<Planets> Planets, string path)
        {
            string jsonWithConverter = JsonConvert.SerializeObject(Planets, new StringEnumConverter());
            File.WriteAllText(SolutionPath + $@"{path}" , jsonWithConverter);
        }


        static public void NGCObjectsCollectionJSONSerialization(List<NGCObjects> NGCObjects, string path)
        {
            string jsonWithConverter = JsonConvert.SerializeObject(NGCObjects, new StringEnumConverter());
            File.WriteAllText(SolutionPath + $@"{path}", jsonWithConverter);
        }


        static public void ConstellationCollectionJSONDeserialization(ref List<Constellations> Constellations, string path)
        {
            try
            {
                using (StreamReader file = File.OpenText(SolutionPath + $@"{path}"))
                {
                    JsonSerializer serializer = new JsonSerializer();
                    string data = file.ReadToEnd();
                    Constellations = JsonConvert.DeserializeObject<List<Constellations>>(data);
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }


        static public void StarsCollectionJSONDeserialization(ref List<Stars> Stars, string path)
        {
            try
            {
                using (StreamReader file = File.OpenText(SolutionPath + $@"{path}"))
                {
                    JsonSerializer serializer = new JsonSerializer();
                    string data = file.ReadToEnd();
                    Stars = JsonConvert.DeserializeObject<List<Stars>>(data);
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }


        static public void PlanetsCollectionJSONDeserialization(ref List<Planets> Planets, string path)
        {
            try
            {
                using (StreamReader file = File.OpenText(SolutionPath + $@"{path}"))
                {
                    JsonSerializer serializer = new JsonSerializer();
                    string data = file.ReadToEnd();
                    Planets = JsonConvert.DeserializeObject<List<Planets>>(data);
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }


        static public void NGCObjectsCollectionJSONDeserialization(ref List<NGCObjects> NGCObjects, string path)
        {
            try
            {
                using (StreamReader file = File.OpenText(SolutionPath + $@"{path}"))
                {
                    JsonSerializer serializer = new JsonSerializer();
                    string data = file.ReadToEnd();
                    NGCObjects = JsonConvert.DeserializeObject<List<NGCObjects>>(data);
                }
            }
            catch (Exception ex)
            {
                return;
            }
        }




        static public void ConstellationCollectionBinarySerialization(List<Constellations> Constellations, string path)
        {
            BinaryFormatter Formatter = new BinaryFormatter();
            using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                Formatter.Serialize(stream, Constellations);
        }


        static public void StarsCollectionBinarySerialization(List<Stars> Stars, string path)
        {
            BinaryFormatter Formatter = new BinaryFormatter();
            using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                Formatter.Serialize(stream, Stars);
        }


        static public void NGCObjectsCollectionBinarySerialization(List<NGCObjects> NGCObjects, string path)
        {
            BinaryFormatter Formatter = new BinaryFormatter();
            using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                Formatter.Serialize(stream, NGCObjects);
        }


        static public void PlanetsCollectionBinarySerialization(List<Planets> Planets, string path)
        {
            BinaryFormatter Formatter = new BinaryFormatter();
            using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                Formatter.Serialize(stream, Planets);
        }
        

        static public void ConstellationCollectionBinaryDeserialization(ref List<Constellations> Constellations, string path)
        {
            try
            {
                BinaryFormatter Formatter = new BinaryFormatter();
                using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                    Constellations = (List<Constellations>)Formatter.Deserialize(stream);
            }
            catch(Exception ex)
            {
                return;
            }
        }


        static public void StarsCollectionBinaryDeserialization(ref List<Stars> Stars, string path)
        {
            try
            {
                BinaryFormatter Formatter = new BinaryFormatter();
                using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                    Stars = (List<Stars>)Formatter.Deserialize(stream);
            }
            catch (Exception ex)
            {
                return;
            }
        }


        static public void NGCObjectsCollectionBinaryDeserialization(ref List<NGCObjects> NGCObjects, string path)
        {
            try
            {
                BinaryFormatter Formatter = new BinaryFormatter();
                using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                    NGCObjects = (List<NGCObjects>)Formatter.Deserialize(stream);
            }
            catch (Exception ex)
            {
                return;
            }
        }


        static public void PlanetsCollectionBinaryDeserialization(ref List<Planets> Planets, string path)
        {
            try
            {
                BinaryFormatter Formatter = new BinaryFormatter();
                using (FileStream stream = new FileStream(SolutionPath + $@"{path}", FileMode.OpenOrCreate))
                    Planets = (List<Planets>)Formatter.Deserialize(stream);
            }
            catch (Exception ex)
            {
                return;
            }
        }
    }
}
