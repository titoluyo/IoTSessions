using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

using System.Text;
using System.Threading.Tasks;
using Microsoft.Azure.Devices.Client;

// The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace IoTDemo
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
            
        }
        private async Task SendDataToAzure(String message)
        {
            DeviceClient deviceClient = DeviceClient.CreateFromConnectionString("HostName=iotsessions.azure-devices.net;DeviceId=DemoIoT;SharedAccessKey=zB0eRB70EvRc8yXo9d1W7eGhja8W8wk3yykucAdImEk=", TransportType.Http1);

            //var text = "Hellow, Windows 10!";
            var msg = new Message(Encoding.UTF8.GetBytes(message));

            await deviceClient.SendEventAsync(msg);
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            var message = txtMessage.Text;
            SendDataToAzure(message);
        }
    }


}
