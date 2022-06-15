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
using System.Windows.Navigation;
using System.Windows.Shapes;
using SpotifyAPI.Web;

namespace adaptPlayer
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            
            InitializeComponent();
            Main();
          
        }

        static async Task Main()
        {
            //Spotify testing
            var config = SpotifyClientConfig.CreateDefault();

            var request = new ClientCredentialsRequest("82ecbf583a174ae29750769f4f49853d", "e5ca52f8663c44c593447e33dc7426d5");
            var response = await new OAuthClient(config).RequestToken(request);

            var spotify = new SpotifyClient(config.WithToken(response.AccessToken));
            var tracks = await spotify.Tracks.Get("1s6ux0lNiTziSrd7iUAADH");
            System.Diagnostics.Debug.WriteLine(tracks.Name);

            var searchItem = new SearchRequest(SearchRequest.Types.All, "Save Me");
            var search = spotify.Search.Item(searchItem);
            System.Diagnostics.Debug.WriteLine("Save me search");
            System.Diagnostics.Debug.WriteLine(search.Result.ToString());
            System.Diagnostics.Debug.WriteLine("Save me search after");

        }

        private void RadioButton_Checked(object sender, RoutedEventArgs e)
        {

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            
            if (RadioButton1.IsChecked == true)
            {
                MessageBox.Show("start button works");
                System.Diagnostics.Debug.WriteLine("Here is Daddy");
            }
            else if (RadioButton2.IsChecked == true)
            {
                MessageBox.Show("stop button is working");
                System.Diagnostics.Debug.WriteLine("Here is Mommy");
            }
        }
    }
}
