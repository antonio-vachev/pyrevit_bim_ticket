import clr
from pyrevit import script
import wpf
import webrequest
from System import Windows

clr.AddReference("System.Windows.Forms")
clr.AddReference("Ironpython.Wpf")

xaml_file = script.get_bundle_file("ui.xaml")

urgency_items = ["Low", "Medium", "High"]
assign_items = ["Anyone", "Radi Karmazov", "Zahari Doychev", "Antonio Vachev","Kiomi Aragaki", "Simeon Tachev", "Danail Momchilov", "Daniel Dimitrov"]
phase_items = ["N/A", "SD", "DD", "CD", "FS"]
consultant_items = [ "N/A", "AR", "EL", "HVAC", "WS", "ST"]
request_items = ["Modeling Issue", "Family", "Bank Files", "Master File", "Automations", "File Error","Shared Coordinates", "Plugins","Exporting", "Other"]
version_items = ["2021", "2020", "2019", "2018", "2017"]

name = __revit__.Application.Username


class MyWindow(Windows.Window):
    def __init__(self):
        wpf.LoadComponent(self, xaml_file)
        self.urgency_combobox.ItemsSource = urgency_items
        self.urgency_combobox.SelectedIndex = 0  
        self.assign_combobox.ItemsSource = assign_items 
        self.assign_combobox.SelectedIndex = 0
        self.consultant_combobox.ItemsSource = consultant_items
        self.consultant_combobox.SelectedIndex = 0  
        self.request_type_combobox.ItemsSource = request_items
        self.request_type_combobox.SelectedIndex = 0
        self.phase_combobox.ItemsSource = phase_items
        self.phase_combobox.SelectedIndex = 0
        self.version_combobox.ItemsSource = version_items
        self.version_combobox.SelectedIndex = 0

    @property
    def urgency(self):
        return self.urgency_combobox.Text

    @property
    def project(self):
        return self.project_textbox.Text

    @property
    def phase(self):
        return self.phase_combobox.Text

    @property
    def consultant(self):
        return self.consultant_combobox.Text

    @property
    def request_type(self):
        return self.request_type_combobox.Text

    @property
    def request(self):
        return self.request_textbox.Text

    @property
    def assign(self):
        return self.assign_combobox.Text

    @property
    def user_id(self):
        if self.assign_combobox.Text == "Radi Karmazov":
            return "448901608953217025"
        elif self.assign_combobox.Text == "Antonio Vachev":
            return "815852881021239317"
        elif self.assign_combobox.Text == "Danail Momchilov":
            return "588741755961344000"
        elif self.assign_combobox.Text == "Simeon Tachev":
            return "588683707766931456"
        elif self.assign_combobox.Text == "Daniel Dimitrov":
            return "841209513591832596"
        elif self.assign_combobox.Text == "Zahari Doychev":
            return "757538079522422834"
        elif self.assign_combobox.Text == "Kiomi Aragaki":
            return "912625699855163403"
        else:
            return "everyone"
    
    @property
    def attachment(self):
        if self.attachment_textbox.Text == "Add URL of your image":
            return "N/A"
        else:
            return self.attachment_textbox.Text

    @property
    def version(self):
        return "R" + self.version_combobox.Text
    
    def submit(self, sender, args):
        webrequest.make_request(self.urgency, self.project, self.phase, name, self.consultant, self.request_type, self.request, self.assign, self.user_id, self.attachment, self.version)
        self.Close()


MyWindow().ShowDialog()

