using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Media.Animation;
using System.Reflection;

using WPF_Material_Design.Source;
using WPF_Material_Design.Forms;
using Plugin;
using System.Configuration;
using TestingWPF;

namespace WPF_Material_Design
{
    public class RelayCommand : ICommand
    {
        private Action<object> execute;
        private Func<object, bool> canExecute;

        // CanExecuteChanged вызывается, когда происходят изменения, которые могут изменить, может ли команда быть выполнена
        public event EventHandler CanExecuteChanged
        {
            add { CommandManager.RequerySuggested += value; }
            remove { CommandManager.RequerySuggested -= value; }
        }


        public RelayCommand(Action<object> execute, Func<object, bool> canExecute = null)
        {
            this.execute = execute;
            this.canExecute = canExecute;
        }

        // CanExecute определит, может ли команда быть выполнена или нет. Если он вернет false, кнопка будет отключена на интерфейсе
        public bool CanExecute(object parameter)
        {
            return this.canExecute == null || this.canExecute(parameter);
        }

        // Execute запускает логику команд
        public void Execute(object parameter)
        {
            this.execute(parameter);
        }
    }


    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        List<Constellations> Constellations = new List<WPF_Material_Design.Source.Constellations>();
        List<Stars> Stars = new List<WPF_Material_Design.Source.Stars>();
        List<NGCObjects> NGCObjects = new List<WPF_Material_Design.Source.NGCObjects>();
        List<Planets> Planets = new List<WPF_Material_Design.Source.Planets>();

        List<Constellations> ConstellationsPrev = new List<WPF_Material_Design.Source.Constellations>();
        List<Stars> StarsPrev = new List<WPF_Material_Design.Source.Stars>();
        List<NGCObjects> NGCObjectsPrev = new List<WPF_Material_Design.Source.NGCObjects>();
        List<Planets> PlanetsPrev = new List<WPF_Material_Design.Source.Planets>();

        List<Constellations> ConstellationsNow = new List<WPF_Material_Design.Source.Constellations>();
        List<Stars> StarsNow = new List<WPF_Material_Design.Source.Stars>();
        List<NGCObjects> NGCObjectsNow = new List<WPF_Material_Design.Source.NGCObjects>();
        List<Planets> PlanetsNow = new List<WPF_Material_Design.Source.Planets>();

        List<Constellations> ConstellationsNext = new List<WPF_Material_Design.Source.Constellations>();
        List<Stars> StarsNext = new List<WPF_Material_Design.Source.Stars>();
        List<NGCObjects> NGCObjectsNext = new List<WPF_Material_Design.Source.NGCObjects>();
        List<Planets> PlanetsNext = new List<WPF_Material_Design.Source.Planets>();


        const int constellations_step = 1;
        const int stars_step = 3;
        const int planets_step = 10;
        const int ngc_step = 10;

        int constellations_pos = 0;
        int stars_pos = 0;
        int ngc_pos = 0;
        int planets_pos = 0;


        Dictionary<string, string> TreeVievFlag = new Dictionary<String, String>();

        private string PluginPath;


        // Список плагинов
        private List<IPlugin> Plugins = new List<IPlugin>();
        static object locker = new object();


        void Update_NowList()
        {
            try
            {
                ConstellationsNow.Clear();
                for (int i = constellations_pos; i < constellations_pos + constellations_step; i++)
                {
                    ConstellationsNow.Add(Constellations[i]);   
                }
            }
            catch (Exception ex)
            { }

            try
            {
                StarsNow.Clear();
                for (int i = stars_pos; i < stars_pos + stars_step; i++)
                    StarsNow.Add(Stars[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                NGCObjectsNow.Clear();
                for (int i = ngc_pos; i < ngc_pos + ngc_step; i++)
                    NGCObjectsNow.Add(NGCObjects[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                PlanetsNow.Clear();
                for (int i = planets_pos; i < planets_pos + planets_step; i++)
                    PlanetsNow.Add(Planets[i]);
            }
            catch (Exception ex)
            { }
        }


        void Update_PrewList()
        {
            try
            {
                ConstellationsPrev.Clear();
                for (int i = constellations_pos; i < constellations_pos + constellations_step; i++)
                    ConstellationsPrev.Add(Constellations[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                StarsPrev.Clear();
                for (int i = stars_pos - stars_step; i < stars_pos; i++)
                    StarsPrev.Add(Stars[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                NGCObjectsPrev.Clear();
                for (int i = ngc_pos - ngc_step; i < ngc_pos; i++)
                    NGCObjectsPrev.Add(NGCObjects[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                PlanetsPrev.Clear();
                for (int i = planets_pos - planets_step + 1; i < planets_pos; i++)
                    PlanetsPrev.Add(Planets[i]);
            }
            catch (Exception ex)
            { }
        }


        void Update_NextList()
        {
            try
            {
                ConstellationsNext.Clear();
                for (int i = constellations_pos + constellations_step - 1; i < constellations_pos + constellations_step * 2 - 1; i++)
                    ConstellationsNext.Add(Constellations[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                StarsNext.Clear();
                for (int i = stars_pos + stars_step; i < stars_pos + stars_step * 2; i++)
                    StarsNext.Add(Stars[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                NGCObjectsNext.Clear();
                for (int i = ngc_pos + ngc_step - 1; i < ngc_pos + ngc_step * 2 - 1; i++)
                    NGCObjectsNext.Add(NGCObjects[i]);
            }
            catch (Exception ex)
            { }

            try
            {
                PlanetsNext.Clear();
                for (int i = planets_pos + planets_step - 1; i < planets_pos + planets_step * 2 - 1; i++)
                    PlanetsNext.Add(Planets[i]);
            }
            catch (Exception ex)
            { }
        }

        bool AllSeqEqual<T>(params IEnumerable<T>[] enumerable)
        {
            for (int i = 0; i < enumerable.Length - 1; i++)
            {
                if (!enumerable[i].SequenceEqual<T>(enumerable[i + 1]))
                    return false;
            }
            return true;
        }


        public MainWindow()
        {
            InitializeComponent();

            Window1 window1 = new Window1();
            window1.ShowDialog();

            TreeVievFlag["lat"] = "Constellations";
            TreeVievFlag["kirlil"] = "Созвездия";

            PluginPath = Directory.GetCurrentDirectory();

            //горячие клавиши
            // Предоставляет метод считывания значений определенного типа из конфигурации
            AppSettingsReader reader = new AppSettingsReader();
            // KeyGestureConverter преобразует объект KeyGesture в другие типы и из других.
            KeyGestureConverter gestureConverter = new KeyGestureConverter();
            try
            {
                PluginPath += (string)reader.GetValue("pluginPath", typeof(string));
            }
            catch(Exception Ex)
            { }

            try
            {
                // Считываем значение ключа Х
                string hotKey = (string)reader.GetValue("Save", typeof(string));
                // KeyGesture определяет комбинацию клавиш, которая может использоваться для вызова команды
                KeyGesture saveKeyGesture = (KeyGesture)gestureConverter.ConvertFromString(hotKey);
                // KeyBinding привязывает KeyGesture к RoutedCommand (или другой реализации ICommand)
                KeyBinding saveKeyBinding = new KeyBinding(new RelayCommand(o =>
                {
                    SerializingCollections.ConstellationCollectionJSONSerialization(Constellations, "RecoveryConstellations.json");
                    SerializingCollections.StarsCollectionJSONSerialization(Stars, "RecoveryStars.json");
                    SerializingCollections.NGCObjectsCollectionJSONSerialization(NGCObjects, "RecoveryNGCObjects.json");
                    SerializingCollections.PlanetsCollectionJSONSerialization(Planets, "RecoveryPlanets.json");

                    MessageBox.Show("Резервная копия создана");

                }, o => true), saveKeyGesture);
                // Добавляем привязку комбинации клавиш
                InputBindings.Add(saveKeyBinding);
            }
            catch { }

            try
            {
                string hotKey = (string)reader.GetValue("Load", typeof(string));
                gestureConverter = new KeyGestureConverter();
                KeyGesture loadKeyGesture = (KeyGesture)gestureConverter.ConvertFromString(hotKey);
                KeyBinding loadKeyBinding = new KeyBinding(new RelayCommand(o =>
                {
                    try
                    {
                        SerializingCollections.ConstellationCollectionJSONDeserialization(ref Constellations, "RecoveryConstellations.json");
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Не удалось загрузить созвездия");
                    }

                    try
                    {
                        SerializingCollections.StarsCollectionJSONDeserialization(ref Stars, "RecoveryStars.json");
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Не удалось загрузить звезды");
                    }

                    try
                    {
                        SerializingCollections.NGCObjectsCollectionJSONDeserialization(ref NGCObjects, "RecoveryNGCObjects.json");
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Не удалось загрузить космические объекты");
                    }

                    try
                    {
                        SerializingCollections.PlanetsCollectionJSONDeserialization(ref Planets, "ecoveryPlanets.json");
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Не удалось загрузить планеты");
                    }

                    UpdateTreeView();
                    MessageBox.Show("Данные восстановлены");

                }, o => true), loadKeyGesture);
                InputBindings.Add(loadKeyBinding);
            }
            catch { }


            // Папка с плагинами и запуск плагинов
            try
            {
                string hotKey = (string)reader.GetValue("Plugins", typeof(string));

                gestureConverter = new KeyGestureConverter();
                KeyGesture pluginsKeyGesture = (KeyGesture)gestureConverter.ConvertFromString(hotKey);
                KeyBinding pluginsKeyBinding = new KeyBinding(new RelayCommand(o =>
                {
                    PluginPath = (string)reader.GetValue("pluginPath", typeof(string));

                    Plugins Wplugins = new Plugins(ref Plugins);
                    Wplugins.Show();

                    string result = "";

                    foreach (var Plugin in Plugins)
                    {
                        try
                        {
                            result = Plugin.Activate();
                        }
                        catch (Exception ex)
                        { }

                        try
                        {
                            Plugin.Activate(Flashback, PluginButton);
                        }
                        catch (Exception ex)
                        { }

                    }
                }, o => true), pluginsKeyGesture);
                InputBindings.Add(pluginsKeyBinding);
            }
            catch { }


            TextBox textBox = new TextBox() { Text = TreeVievFlag["kirlil"] };
            MainTreeView.Items.Add(textBox);


            SerializingCollections.ConstellationCollectionBinaryDeserialization(ref Constellations, "Constellations.dat");
            //SerializingCollections.ConstellationCollectionJSONDeserialization(ref Constellations, @"Constellations.json");

            SerializingCollections.StarsCollectionJSONDeserialization(ref Stars, "Stars.json");
            SerializingCollections.NGCObjectsCollectionJSONDeserialization(ref NGCObjects, "NGCObjects.json");
            SerializingCollections.PlanetsCollectionJSONDeserialization(ref Planets, "Planets.json");

            
            // Заполняем список плагинов в отдельном потоке
            Thread pluginsSearchThread = new Thread(new ThreadStart(RefreshPlugins));
            pluginsSearchThread.Start();


            Update_NowList();
            Update_PrewList();
            Update_NextList();

            UpdateTreeView();

            Page.Content = constellations_pos + 1;
        }



        private void UpdateTreeView()
        {
            if (TreeVievFlag["lat"] == "Constellations")
            {
                SerializingCollections.ConstellationCollectionJSONSerialization(Constellations, "Constellations.json");
                SerializingCollections.ConstellationCollectionBinarySerialization(Constellations, "Constellations.dat");
;
                ShowItems.ShowConstellations(ref MainTreeView, ref ConstellationsNow, ref Stars, ref NGCObjects, ref Planets, TreeVievFlag);

            }
                

            else if (TreeVievFlag["lat"] == "Stars")
            {
                SerializingCollections.StarsCollectionJSONSerialization(Stars, "Stars.json");
                SerializingCollections.StarsCollectionBinarySerialization(Stars, "Stars.dat");

                ShowItems.ShowStars(ref MainTreeView, ref StarsNow, ref Planets, TreeVievFlag);
            }


            else if (TreeVievFlag["lat"] == "NGCObjects")
            {
                SerializingCollections.NGCObjectsCollectionJSONSerialization(NGCObjects, "NGCObjects.json");
                SerializingCollections.NGCObjectsCollectionBinarySerialization(NGCObjects, "NGCObjects.dat");

                ShowItems.ShowNGCObjects(ref MainTreeView, ref NGCObjectsNow, TreeVievFlag);
            }


            else if (TreeVievFlag["lat"] == "Planets")
            {
                SerializingCollections.PlanetsCollectionJSONSerialization(Planets, "Planets.json");
                SerializingCollections.PlanetsCollectionBinarySerialization(Planets, "Planets.dat");

                ShowItems.ShowPlanets(ref MainTreeView, ref PlanetsNow, TreeVievFlag);
            }
        }




        private void InfoPanel_Constellations(Constellations constellation)
        {
            Key_1.Text = "Созвездие:";         
            Key_2.Text = "Склонение от:";
            Key_3.Text = "Склонение до:";
            Key_4.Text = "Прямое восхождение от:";
            Key_5.Text = "Прямое восхождение до:";
            Key_6.Text = "";
            Key_7.Text = "";
            Key_8.Text = "";
            Key_9.Text = "";
            Key_10.Text = "";

            Answer_1.Text = constellation.Name;
            Answer_2.Text = Convert.ToString(constellation.Declination_from);
            Answer_3.Text = Convert.ToString(constellation.Declination_to);
            Answer_4.Text = Convert.ToString(constellation.Right_Ascension_from);
            Answer_5.Text = Convert.ToString(constellation.Right_Ascension_to);
            Answer_6.Text = "";
            Answer_7.Text = "";
            Answer_8.Text = "";
            Answer_9.Text = "";
            Answer_10.Text = "";

            InfoBlock.Text = constellation.Info;
        }


        private void InfoPanel_Stars(Stars star)
        {
            Key_1.Text = "Имя звезды:";
            Key_2.Text = "Созвездие:";
            Key_3.Text = "Склонение:";
            Key_4.Text = "Прямое восхождение:";
            Key_5.Text = "Масса звезды:";
            Key_6.Text = "Радиус звезды:";
            Key_7.Text = "Видимая звездная величина:";
            Key_8.Text = "Светимость звезды:";
            Key_9.Text = "Тип звезды:";
            Key_10.Text = "";

            Answer_1.Text = star.Name;
            Answer_2.Text = star.Constellatoin;
            Answer_3.Text = Convert.ToString(star.Declination);
            Answer_4.Text = Convert.ToString(star.Right_Ascension);
            Answer_5.Text = Convert.ToString(star.Weight);
            Answer_6.Text = Convert.ToString(star.Radius);
            Answer_7.Text = Convert.ToString(star.Apparent_Star_Magnitude);
            Answer_8.Text = Convert.ToString(star.Star_Luminosity);
            Answer_9.Text = star.Star_Type;
            Answer_10.Text = "";

            InfoBlock.Text = star.Info;
        }


        private void InfoPanel_NGCObjects(NGCObjects NGCObject)
        {
            Key_1.Text = "Имя объекта:";
            Key_2.Text = "Созвездие:";
            Key_3.Text = "Склонение:";
            Key_4.Text = "Прямое восхождение:";
            Key_5.Text = "Видимая звездная величина:";
            Key_6.Text = "Красное смещение:";
            Key_7.Text = "Расстояние:";
            Key_8.Text = "Тип:";
            Key_9.Text = "";
            Key_10.Text = "";

            Answer_1.Text = NGCObject.Name;
            Answer_2.Text = NGCObject.Constellatoin;
            Answer_3.Text = Convert.ToString(NGCObject.Declination);
            Answer_4.Text = Convert.ToString(NGCObject.Right_Ascension);
            Answer_5.Text = Convert.ToString(NGCObject.Apparent_Star_Magnitude);
            Answer_6.Text = Convert.ToString(NGCObject.Redshift);
            Answer_7.Text = Convert.ToString(NGCObject.Distance);
            Answer_8.Text = Convert.ToString(NGCObject.Type);
            Answer_9.Text = "";
            Answer_10.Text = "";

            InfoBlock.Text = NGCObject.Info;
        }


        private void InfoPanel_Planets(Planets planet)
        {
            Key_1.Text = "Имя планеты:";
            Key_2.Text = "Радиус планеты:";
            Key_3.Text = "Масса планеты:";
            Key_4.Text = "Период обращения вокруг тела:";
            Key_5.Text = "Период обращения вокруг оси:";
            Key_6.Text = "Главное тело:";
            Key_7.Text = "Радиус орбиты:";
            Key_8.Text = "Эксцентриситет";
            Key_9.Text = "";
            Key_10.Text = "";

            Answer_1.Text = planet.Name;
            Answer_2.Text = Convert.ToString(planet.Radius);
            Answer_3.Text = Convert.ToString(planet.Weight);
            Answer_4.Text = Convert.ToString(planet.Circulation_Period_Axis);
            Answer_5.Text = Convert.ToString(planet.Circulation_Period);
            Answer_6.Text = Convert.ToString(planet.Center_body);
            Answer_7.Text = Convert.ToString(planet.Orbit_Radius);
            Answer_8.Text = Convert.ToString(planet.Eccentricity);
            Answer_9.Text = "";
            Answer_10.Text = "";

            InfoBlock.Text = Convert.ToString(planet.Info);
        }


       

        private void add_to_cental_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                TreeViewItem selectedTVI = (TreeViewItem)MainTreeView.SelectedItem;
                if (selectedTVI != null)
                {
                    if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Stars")
                    {
                        int i = Planets.Count();

                        PlanetsDialogHost DialogWindow = new PlanetsDialogHost(ref Planets);
                        DialogWindow.ShowDialog();

                        if (i == Planets.Count())
                            return;

                        Update_NowList();
                        Update_PrewList();
                        Update_NextList();

                        UpdateTreeView();

                        return;
                    }



                    else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Planets")
                    {
                        int i = Planets.Count();

                        PlanetsDialogHost DialogWindow = new PlanetsDialogHost(ref Planets);
                        DialogWindow.ShowDialog();

                        if (i == Planets.Count())
                            return;

                        Update_NowList();
                        Update_PrewList();
                        Update_NextList();

                        UpdateTreeView();
                        return;
                    }

                    else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "NGCObjects")
                    {
                        int i = NGCObjects.Count();

                        NGCObjectsDialogHost DialogWindow = new NGCObjectsDialogHost(ref NGCObjects);
                        DialogWindow.ShowDialog();

                        if (i == NGCObjects.Count())
                            return;

                        Update_NowList();
                        Update_PrewList();
                        Update_NextList();

                        UpdateTreeView();

                        return;
                    }

                    else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Constellations")
                    {
                        int i = Stars.Count();

                        StarsDialogHost DialogWindow = new StarsDialogHost(ref Stars);
                        DialogWindow.ShowDialog();

                        if (i == Stars.Count())
                            return;

                        Update_NowList();
                        Update_PrewList();
                        Update_NextList();

                        UpdateTreeView();
                        return;
                    }
                }


                else if (TreeVievFlag["lat"] == "Constellations")
                {
                    int i = Constellations.Count();
                    ConstellationsDialogHost DialogWindow = new ConstellationsDialogHost(ref Constellations);
                    DialogWindow.ShowDialog();
                    if (i == Constellations.Count())
                        return;

                    Update_NowList();
                    Update_PrewList();
                    Update_NextList();

                    UpdateTreeView();
                    return;
                }

                else if (TreeVievFlag["lat"] == "NGCObjects")
                {
                    int i = NGCObjects.Count();
                    NGCObjectsDialogHost DialogWindow = new NGCObjectsDialogHost(ref NGCObjects);
                    DialogWindow.ShowDialog();
                    if (i == NGCObjects.Count())
                        return;

                    UpdateTreeView();
                    return;
                }

                else if (TreeVievFlag["lat"] == "Stars")
                {
                    int i = Stars.Count();
                    StarsDialogHost DialogWindow = new StarsDialogHost(ref Stars);
                    DialogWindow.ShowDialog();

                    if (i == Stars.Count())
                        return;

                    Update_NowList();
                    Update_PrewList();
                    Update_NextList();

                    UpdateTreeView();
                    return;
                }

                else if (TreeVievFlag["lat"] == "Planets")
                {
                    int i = Planets.Count();
                    PlanetsDialogHost DialogWindow = new PlanetsDialogHost(ref Planets);
                    DialogWindow.ShowDialog();

                    if (i == Planets.Count())
                        return;

                    Update_NowList();
                    Update_PrewList();
                    Update_NextList();

                    UpdateTreeView();
                    return;
                }
            }
            
            catch(Exception ex)
            {
                return;
            }
        }


        private void edit_in_right_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                TreeViewItem selectedTVI = (TreeViewItem)MainTreeView.SelectedItem;

                if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Planets")
                {
                    int i = Planets.Count();

                    foreach (Planets planet in Planets)
                    {
                        if (planet.Name.Equals(selectedTVI.Header))
                        {
                            PlanetsDialogHost DialogWindow = new PlanetsDialogHost(planet);
                            DialogWindow.ShowDialog();

                            Update_NowList();
                            Update_PrewList();
                            Update_NextList();

                            UpdateTreeView();
                            InfoPanel_Planets(planet);
                            break;
                        }
                    }
                    return;
                }



                else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Stars")
                {
                    int i = Stars.Count();

                    foreach (Stars star in Stars)
                    {
                        if (star.Name.Equals(selectedTVI.Header))
                        {
                            StarsDialogHost DialogWindow = new StarsDialogHost(star);
                            DialogWindow.ShowDialog();

                            Update_NowList();
                            Update_PrewList();
                            Update_NextList();

                            UpdateTreeView();
                            InfoPanel_Stars(star);
                            break;
                        }
                    }

                    return;
                }

                else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "NGCObjects")
                {
                    int i = NGCObjects.Count();

                    foreach (NGCObjects NGCObject in NGCObjects)
                    {
                        if (NGCObject.Name.Equals(selectedTVI.Header))
                        {
                            NGCObjectsDialogHost DialogWindow = new NGCObjectsDialogHost(NGCObject);
                            DialogWindow.ShowDialog();

                            Update_NowList();
                            Update_PrewList();
                            Update_NextList();

                            UpdateTreeView();
                            InfoPanel_NGCObjects(NGCObject);
                            break;
                        }
                    }
                    return;

                }

                else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Constellations")
                {
                    int i = Stars.Count();

                    foreach (Constellations constellation in Constellations)
                    {
                        if (constellation.Name.Equals(selectedTVI.Header))
                        {
                            ConstellationsDialogHost DialogWindow = new ConstellationsDialogHost(constellation);
                            DialogWindow.ShowDialog();

                            Update_NowList();
                            Update_PrewList();
                            Update_NextList();

                            UpdateTreeView();
                            InfoPanel_Constellations(constellation);
                            break;
                        }
                    }

                    return;
                }
            }

            catch (Exception ex)
            {
                return;
            }
        }


        private void delete_from_center_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                TreeViewItem selectedTVI = (TreeViewItem)MainTreeView.SelectedItem;

                Delete_from_TreeView(selectedTVI);

                Update_NowList();
                Update_PrewList();
                Update_NextList();

                UpdateTreeView();
            }

            catch (Exception ex)
            {
                return;
            }
        }


        private void delete_from_right_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                TreeViewItem selectedTVI = (TreeViewItem)MainTreeView.SelectedItem;

                Delete_from_TreeView(selectedTVI);

                Update_NowList();
                Update_PrewList();
                Update_NextList();

                UpdateTreeView();
            }

            catch (Exception ex)
            {
                return;
            }
        }



        private void Delete_from_TreeView(TreeViewItem selectedTVI)
        {
            if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")).Equals("Planets"))
            {
                int i = Planets.Count();

                foreach (Planets planet in Planets)
                {
                    if (planet.Name.Equals(selectedTVI.Header))
                    {
                        Planets.Remove(planet);

                        planets_pos--;

                        UpdateTreeView();
                        break;
                    }
                }
                return;
            }

            else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")).Equals("Stars"))
            {
                int i = Stars.Count();

                foreach (Stars star in Stars)
                {
                    if (star.Name.Equals(selectedTVI.Header))
                    {
                        Stars.Remove(star);

                        stars_pos--;

                        UpdateTreeView();
                        break;
                    }
                }
                return;
            }

            else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")).Equals("Constellations"))
            {
                int i = Constellations.Count();

                foreach (Constellations constellation in Constellations)
                {
                    if (constellation.Name.Equals(selectedTVI.Header))
                    {
                        Constellations.Remove(constellation);

                        constellations_pos--;

                        UpdateTreeView();
                        break;
                    }
                }
                return;
            }

            else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")).Equals("NGCObjects"))
            {
                int i = NGCObjects.Count();

                foreach (NGCObjects ngcObject in NGCObjects)
                {
                    if (ngcObject.Name.Equals(selectedTVI.Header))
                    {
                        NGCObjects.Remove(ngcObject);

                        ngc_pos--;

                        UpdateTreeView();
                        break;
                    }
                }
                return;
            }
        }




        private void constallations_Click(object sender, RoutedEventArgs e)
        {
            TreeVievFlag["lat"] = "Constellations";
            TreeVievFlag["kirlil"] = "Созвездия";

            NGCstackPanel.Visibility = Visibility.Hidden;
            StarsStackPanel.Visibility = Visibility.Hidden;

            Show_NGC_CheckBox.Visibility = Visibility.Hidden;
            Show_Stars_CheckBox.Visibility = Visibility.Hidden;

            UpdateTreeView();
        }


        private void stars_Click(object sender, RoutedEventArgs e)
        {
            TreeVievFlag["lat"] = "Stars";
            TreeVievFlag["kirlil"] = "Звезды";

            NGCstackPanel.Visibility = Visibility.Hidden;
            StarsStackPanel.Visibility = Visibility.Visible;
            
            Show_NGC_CheckBox.Visibility = Visibility.Hidden;
            Show_Stars_CheckBox.Visibility = Visibility.Visible;

            UpdateTreeView();
        }


        private void ngcObjects_Click(object sender, RoutedEventArgs e)
        {
            TreeVievFlag["lat"] = "NGCObjects";
            TreeVievFlag["kirlil"] = "Космические объекты";

            NGCstackPanel.Visibility = Visibility.Visible;
            StarsStackPanel.Visibility = Visibility.Hidden;
            
            Show_NGC_CheckBox.Visibility = Visibility.Visible;
            Show_Stars_CheckBox.Visibility = Visibility.Hidden;

            UpdateTreeView();
        }


        private void planets_Click(object sender, RoutedEventArgs e)
        {
            TreeVievFlag["lat"] = "Planets";
            TreeVievFlag["kirlil"] = "Планеты";

            NGCstackPanel.Visibility = Visibility.Hidden;
            StarsStackPanel.Visibility = Visibility.Hidden;
            
            Show_NGC_CheckBox.Visibility = Visibility.Hidden;
            Show_Stars_CheckBox.Visibility = Visibility.Hidden;

            UpdateTreeView();
        }

                

        private void MainTreeView_SelectedItemChanged(object sender, RoutedPropertyChangedEventArgs<object> e)
        {
            try
            {
                TreeViewItem selectedTVI = (TreeViewItem)MainTreeView.SelectedItem;

                if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Planets")
                {
                    int i = Planets.Count();

                    foreach (Planets planet in Planets)
                    {
                        if (planet.Name.Equals(selectedTVI.Header))
                        {
                            InfoPanel_Planets(planet);
                            break;
                        }
                    }
                    return;
                }



                else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Stars")
                {
                    int i = Stars.Count();

                    foreach (Stars star in Stars)
                    {
                        if (star.Name.Equals(selectedTVI.Header))
                        {
                            InfoPanel_Stars(star);
                            break;
                        }
                    }
                    return;
                }

                else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "NGCObjects")
                {
                    int i = NGCObjects.Count();

                    foreach (NGCObjects NGCObject in NGCObjects)
                    {
                        if (NGCObject.Name.Equals(selectedTVI.Header))
                        {
                            InfoPanel_NGCObjects(NGCObject);
                            break;
                        }
                    }
                    return;
                }

                else if (selectedTVI.Name.Substring(0, selectedTVI.Name.IndexOf("_")) == "Constellations")
                {
                    int i = Stars.Count();

                    foreach (Constellations constellation in Constellations)
                    {
                        if (constellation.Name.Equals(selectedTVI.Header))
                        {
                            InfoPanel_Constellations(constellation);
                            break;
                        }
                    }
                    return;
                }

            }
            
            catch (Exception ex)
            {
                return;
            }
        }




        private void RecoveryCreate_Click(object sender, RoutedEventArgs e)
        {
            SerializingCollections.ConstellationCollectionJSONSerialization(Constellations, "RecoveryConstellations.json");
            SerializingCollections.StarsCollectionJSONSerialization(Stars, "RecoveryStars.json");
            SerializingCollections.NGCObjectsCollectionJSONSerialization(NGCObjects, "RecoveryNGCObjects.json");
            SerializingCollections.PlanetsCollectionJSONSerialization(Planets, "RecoveryPlanets.json");

            MessageBox.Show("Резервная копия создана");
        }


        private void RecoveryLoad_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                SerializingCollections.ConstellationCollectionJSONDeserialization(ref Constellations, "RecoveryConstellations.json");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Не удалось загрузить созвездия");
            }

            try
            {
                SerializingCollections.StarsCollectionJSONDeserialization(ref Stars, "RecoveryStars.json");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Не удалось загрузить звезды");
            }

            try
            {
                SerializingCollections.NGCObjectsCollectionJSONDeserialization(ref NGCObjects, "RecoveryNGCObjects.json");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Не удалось загрузить космические объекты");
            }

            try
            {
                SerializingCollections.PlanetsCollectionJSONDeserialization(ref Planets, "ecoveryPlanets.json");
            }
            catch (Exception ex)
            {
                MessageBox.Show("Не удалось загрузить планеты");
            }

            UpdateTreeView();
            MessageBox.Show("Данные восстановлены");
        }



        private void RefreshPlugins()
        {
            lock (locker)
            {
                Plugins.Clear();

                // Класс DirectoryInfo - Предоставляет методы экземпляра класса для создания, перемещения и перечисления в каталогах и подкаталогах
                DirectoryInfo PluginDirectory = new DirectoryInfo(PluginPath);
                if (!PluginDirectory.Exists)
                    PluginDirectory.Create();

                // Класс Directory - Предоставляет статические методы для создания, перемещения и перечисления в каталогах и вложенных каталогах
                // Возвращает имена файлов (с указанием пути к ним) в указанном каталоге 
                // с расширением .dll  
                var PluginFiles = Directory.GetFiles(PluginPath, "*.dll");

                // Среди всех объектов
                foreach (var File in PluginFiles)
                {
                    // Класс Assembly - Представляет сборку, которая является модулем с возможностью многократного использования
                    // LoadFrom(File) - Загружает сборку с заданным именем или путем
                    Assembly Assembly = Assembly.LoadFrom(File);


                    // GetTypes() - Получает типы, определенные в этой сборке, реализующие наш интерфейс IPlugin,
                    // Where - Выполняет фильтрацию последовательности значений на основе заданного предиката typeof(IPlugin)
                    var Types = Assembly.GetTypes().
                                    Where(t => t.GetInterfaces().                                   // получить все интерфейсы в сборке
                                    Where(i => i.FullName == typeof(IPlugin).FullName).Any());      // типа IPlugin
       

                    foreach (var type in Types)
                    {
                        var plugin = Assembly.CreateInstance(type.FullName) as IPlugin;             // Находит заданный тип в этой сборке и создает его экземпляр, используя абстрактный метод.
                        Plugins.Add(plugin);
                    }
                }
            }
        }

        private void PluginsON_Click(object sender, RoutedEventArgs e)
        {
            Plugins Wplugins = new Plugins(ref Plugins);
            Wplugins.Show();

            string result = "";

            foreach (var Plugin in Plugins)
            {
                try
                {
                    result = Plugin.Activate();
                }
                catch(Exception ex)
                { }

                try
                {
                    Plugin.Activate(Flashback, PluginButton);
                }
                catch(Exception ex)
                { }
            }
        }



        private void PluginsOFF_Click(object sender, RoutedEventArgs e)
        {
            Flashback.Visibility = Visibility.Hidden;
            PluginButton.Visibility = Visibility.Hidden;

            System.Media.SoundPlayer player = new System.Media.SoundPlayer("Creedence_Clearwater_Revival_-_Fortunate_Son.wav");
            player.Stop();
        }

        private void PluginButton_Click(object sender, RoutedEventArgs e)
        {
            Flashback.Visibility = Visibility.Hidden;
            PluginButton.Visibility = Visibility.Hidden;

            System.Media.SoundPlayer player = new System.Media.SoundPlayer("Creedence_Clearwater_Revival_-_Fortunate_Son.wav");
            player.Stop();

        }



        

        private void Search_TextChanged(object sender, TextChangedEventArgs e)
        {
            if (TreeVievFlag["lat"].Equals("Constellations"))
            {
                IEnumerable<Constellations> selectedConstellation = from Constellation in Constellations
                                                   where Constellation.Name.Contains(Search.Text)
                                                   orderby Constellation.Name
                                                   select Constellation;

                ShowItems.ShowConstellations(ref MainTreeView, ref selectedConstellation, ref Stars, ref NGCObjects, ref Planets, TreeVievFlag);
            }

            else if (TreeVievFlag["lat"].Equals("Stars"))
            {
                IEnumerable<Stars> selectedStars = from Star in Stars
                                                   where Star.Name.Contains(Search.Text)
                                                   orderby Star.Name
                                                   select Star;
                ShowItems.ShowStars(ref MainTreeView, ref selectedStars, ref Planets, TreeVievFlag);
            }

            else if (TreeVievFlag["lat"].Equals("NGCObjects"))
            {
                IEnumerable<NGCObjects> selectedNGCObjects = from NGCobject in NGCObjects
                                                             where NGCobject.Name.Contains(Search.Text)
                                                             orderby NGCobject.Name
                                                             select NGCobject;

                ShowItems.ShowNGCObjects(ref MainTreeView, ref selectedNGCObjects, TreeVievFlag);
            }

            else if (TreeVievFlag["lat"].Equals("Planets"))
            {
                IEnumerable<Planets> selectedPlanets = from Planet in Planets
                                                          where Planet.Name.Contains(Search.Text)
                                                             orderby Planet.Name
                                                             select Planet;

                ShowItems.ShowPlanets(ref MainTreeView, ref selectedPlanets, TreeVievFlag);
            }
        }


        private void Show_NGC_CheckBox_Click(object sender, RoutedEventArgs e)
        {
            IEnumerable<NGCObjects> selectedNGCObjects = new List<Source.NGCObjects>();

            var newNGCs = from ngc in NGCObjects
                          group ngc by ngc.Type;

            string res = null;
            foreach (var g in newNGCs)
            {
                res += g.Key + ":\n";
                
                foreach (var constell in g)
                {
                    res += constell.Name + ",\n";
                }
                res += "\n";
            }

            System.Windows.MessageBox.Show(res);

            if (Nebula.IsChecked == true)
            {
                try
                {
                    IEnumerable<NGCObjects> _selectedNGCObjects = from NGCobject in NGCObjects.AsParallel().AsOrdered()     // выбираем объект
                                                                  where NGCobject.Type.Equals("Туманность")                 // определяем каждый объект из teams как t
                                                                  orderby NGCobject.Name                                    // фильтрация по критерию
                                                                  select NGCobject;                                         // упорядочиваем по возрастанию

                    selectedNGCObjects = selectedNGCObjects.Union(_selectedNGCObjects.ToList());
                }
                catch (Exception ex)
                { }
            }

            if (Open_cluster.IsChecked == true)
            {
                try
                {
                    IEnumerable<NGCObjects> _selectedNGCObjects =  from NGCobject in NGCObjects.AsParallel().AsOrdered()
                                                                   where NGCobject.Type.Contains("Рассеянное")
                                                                   orderby NGCobject.Name
                                                                   select NGCobject;                                        

                    selectedNGCObjects = selectedNGCObjects.Union(_selectedNGCObjects.ToList());
                }
                catch(Exception ex)
                { }

            }

            if (Planetary_nebulae.IsChecked == true)
            {
                try
                {
                    IEnumerable<NGCObjects> _selectedNGCObjects = from NGCobject in NGCObjects.AsParallel().AsOrdered()
                                                                  where NGCobject.Type.Contains("Планетарная")
                                                                  orderby NGCobject.Name
                                                                  select NGCobject;

                    selectedNGCObjects = selectedNGCObjects.Union(_selectedNGCObjects.ToList());
                }
                catch (Exception ex)
                { }
            }

            if (Globular_cluster.IsChecked == true)
            {
                try
                {
                    IEnumerable<NGCObjects> _selectedNGCObjects = from NGCobject in NGCObjects.AsParallel().AsOrdered()
                                                                  where NGCobject.Type.Contains("Шаровое")
                                                                  orderby NGCobject.Name
                                                                  select NGCobject;

                    selectedNGCObjects = selectedNGCObjects.Union(_selectedNGCObjects.ToList());
                }
                catch(Exception ex)
                { }
            }

            if (Galaxy.IsChecked == true)
            {
                try
                {
                    IEnumerable<NGCObjects> _selectedNGCObjects = from NGCobject in NGCObjects.AsParallel().AsOrdered()
                                                                  where NGCobject.Type.Contains("Галактика")
                                                                  orderby NGCobject.Name
                                                                  select NGCobject;

                    selectedNGCObjects = selectedNGCObjects.Union(_selectedNGCObjects.ToList());
                }
                catch(Exception ex)
                { }
            }

            ShowItems.ShowNGCObjects(ref MainTreeView, ref selectedNGCObjects, TreeVievFlag);
        }

        private void Show_Stars_CheckBox_Click(object sender, RoutedEventArgs e)
        {
            IEnumerable<Stars> selectedStars = new List<Source.Stars>();

            var newStars = from star in Stars
                           orderby star.Name
                           group star by star.Star_Type;

            string res = null;
            foreach (var g in newStars)
            {
                res += g.Key + ":\n";

                foreach (var constell in g)
                {
                    res += constell.Name + ",\n";
                }
                res += "\n";
            }

            System.Windows.MessageBox.Show(res);


            if (Class_O.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("O") || Star.Star_Type.Contains("О")
                                                   orderby Star.Name
                                                   select Star;


            }

            if (Class_B.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("B") || Star.Star_Type.Contains("В")
                                                   orderby Star.Name
                                                   select Star;
                selectedStars = selectedStars.Union(_selectedStars.ToList());
            }

            if (Class_A.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("A") || Star.Star_Type.Contains("А")
                                                   orderby Star.Name
                                                   select Star;

                selectedStars = selectedStars.Union(_selectedStars.ToList());
            }

            if (Class_F.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("F")
                                                   orderby Star.Name
                                                   select Star;

                selectedStars = selectedStars.Union(_selectedStars.ToList());
            }

            if (Class_G.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("G")
                                                   orderby Star.Name
                                                   select Star;

                selectedStars = selectedStars.Union(_selectedStars.ToList());
            }

            if (Class_K.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("K") || Star.Star_Type.Contains("К")
                                                   orderby Star.Name
                                                   select Star;

                selectedStars = selectedStars.Union(_selectedStars.ToList());
            }

            if (Class_M.IsChecked == true)
            {
                IEnumerable<Stars> _selectedStars = from Star in Stars.AsParallel().AsOrdered()
                                                   where Star.Star_Type.Contains("M") || Star.Star_Type.Contains("М")
                                                   orderby Star.Name
                                                   select Star;
            
                selectedStars = selectedStars.Union(_selectedStars.ToList());
            }

            IEnumerable<Stars> __selectedStars = from Star in selectedStars.AsParallel().AsOrdered()
                                               orderby Star.Name
                                               select Star;

            selectedStars = selectedStars.Union(__selectedStars.ToList());

            ShowItems.ShowStars(ref MainTreeView, ref selectedStars, ref Planets, TreeVievFlag);
        }



        private void move_right_Click(object sender, RoutedEventArgs e)
        {
            if (TreeVievFlag["lat"] == "Constellations")
            {
                if (Constellations.Count <= constellations_pos + constellations_step)
                    return;

                ConstellationsPrev = ConstellationsNow;
                ConstellationsNow = ConstellationsNext;
                

                Thread pagesThread = new Thread(new ThreadStart(Update_NextList));
                pagesThread.Start();

                constellations_pos += constellations_step;
                Page.Content = constellations_pos + 1;

                UpdateTreeView();
            }


            else if (TreeVievFlag["lat"] == "Stars")
            {
                if (Stars.Count <= stars_pos + stars_step)
                    return;

                StarsPrev = StarsNow;
                StarsNow = StarsNext;


                Thread pagesThread = new Thread(new ThreadStart(Update_NextList));
                pagesThread.Start();

                stars_pos += stars_step;
                Page.Content = stars_pos + 1;

                UpdateTreeView();

            }


            else if (TreeVievFlag["lat"] == "NGCObjects")
            {
                if (NGCObjects.Count <= ngc_pos + ngc_step)
                    return;

                NGCObjectsPrev  = NGCObjectsNow;
                NGCObjectsNow = NGCObjectsNext;


                Thread pagesThread = new Thread(new ThreadStart(Update_NextList));
                pagesThread.Start();

                ngc_pos += ngc_step;
                Page.Content = ngc_pos + 1;

                UpdateTreeView();
            }


            else if (TreeVievFlag["lat"] == "Planets")
            {
                if (Planets.Count <= planets_pos + planets_step)
                    return;

                PlanetsPrev  = PlanetsNow;
                PlanetsNow = PlanetsNext;


                Thread pagesThread = new Thread(new ThreadStart(Update_NextList));
                pagesThread.Start();

                planets_pos += planets_step;
                Page.Content = planets_pos + 1;

                UpdateTreeView();
            }
        }

        private void move_left_Click(object sender, RoutedEventArgs e)
        {           
            if (TreeVievFlag["lat"] == "Constellations")
            {
                if (constellations_pos <= 0)
                    return;

                ConstellationsNext = ConstellationsNow;
                ConstellationsNow = ConstellationsPrev;


                Thread pagesThread = new Thread(new ThreadStart(Update_PrewList));
                pagesThread.Start();

                constellations_pos -= constellations_step;
                Page.Content = constellations_pos + 1;

                UpdateTreeView();
            }


            else if (TreeVievFlag["lat"] == "Stars")
            {
                if (stars_pos <= stars_step)
                    return;

                StarsNext = StarsNow;
                StarsNow = StarsPrev;


                Thread pagesThread = new Thread(new ThreadStart(Update_PrewList));
                pagesThread.Start();

                stars_pos -= stars_step;
                Page.Content = stars_pos + 1;

                UpdateTreeView();

            }


            else if (TreeVievFlag["lat"] == "NGCObjects")
            {
                if (ngc_pos <= 0)
                    return;

                NGCObjectsNext = NGCObjectsNow;
                NGCObjectsNow = NGCObjectsPrev;


                Thread pagesThread = new Thread(new ThreadStart(Update_PrewList));
                pagesThread.Start();

                ngc_pos -= ngc_step;
                Page.Content = ngc_pos + 1;

                UpdateTreeView();
            }


            else if (TreeVievFlag["lat"] == "Planets")
            {
                if (planets_pos <= 0)
                    return;

                PlanetsNext = PlanetsNow;
                PlanetsNow = PlanetsPrev;


                Thread pagesThread = new Thread(new ThreadStart(Update_PrewList));
                pagesThread.Start();

                planets_pos -= planets_step;
                Page.Content = planets_pos + 1;

                UpdateTreeView();
            }
        }

        private void exlog_MouseEnter(object sender, MouseEventArgs e)
        {
            exlog_pic.Visibility = Visibility.Visible;
        }

        private void exlog_MouseLeave(object sender, MouseEventArgs e)
        {
            exlog_pic.Visibility = Visibility.Hidden;
        }
    }
}
    