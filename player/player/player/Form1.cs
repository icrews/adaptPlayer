using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace player
{
    public partial class Form1 : Form
    {
        private Mp3Player mp3Player = new Mp3Player();
        public Form1()
        {
            InitializeComponent();
            customizeDesign();
        }

        #region subButtons
        private void button2_Click(object sender, EventArgs e)
        {
            openChildForm(new Form2());
            hideSubMenu();
        }
        private void button3_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }
        private void button4_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }

        private void btnImport_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
            using (OpenFileDialog ofd = new OpenFileDialog())
            {
                ofd.Filter = "Mp3 Files|*.mp3";
                if (ofd.ShowDialog() == DialogResult.OK)
                {
                    mp3Player.open(ofd.FileName);
                }
            }
        }


        private void button7_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }
        private void button8_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }
        private void button9_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }
        private void button14_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }
        private void button15_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            // Codes
            hideSubMenu();
        }

        #endregion

        #region functionality
        private void customizeDesign()
        {
            panelMediaSubmenu.Visible = false;
            panelPlaylistSubmenu.Visible = false;
            panelToolsSubmenu.Visible = false;
            //..
        }

        private void hideSubMenu()
        { 
            if (panelMediaSubmenu.Visible == true)
                panelMediaSubmenu.Visible = false; 
            if (panelPlaylistSubmenu.Visible == true)
                panelPlaylistSubmenu.Visible = false; 
            if (panelToolsSubmenu.Visible == true)
                panelToolsSubmenu.Visible = false;

        }

        private void showSubMenu(Panel subMenu)
        {
            if (subMenu.Visible == false)
            {
                hideSubMenu();
                subMenu.Visible = true;
            }
            else 
                subMenu.Visible = false;
        }

        #endregion

        #region primaryButtons
        private void btnMedia_Click(object sender, EventArgs e)
        {
            showSubMenu(panelMediaSubmenu);
        }

        private void btnTools_Click(object sender, EventArgs e)
        {
            showSubMenu(panelToolsSubmenu);
        }

        private void btnHelp_Click(object sender, EventArgs e)
        {
            hideSubMenu();
        }

        private void btnPlaylist_Click(object sender, EventArgs e)
        {
            showSubMenu(panelPlaylistSubmenu);
        }
        #endregion

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private Form activeForm = null;

        private void openChildForm(Form childForm)
        {
            if (activeForm != null)
                activeForm.Close();
            activeForm = childForm;
            childForm.TopLevel = false;
            childForm.FormBorderStyle = FormBorderStyle.None;
            childForm.Dock = DockStyle.Fill;
            panelChildForm.Controls.Add(childForm);
            panelChildForm.Tag = childForm;
            childForm.BringToFront();
            childForm.Show();
        }

        private void btnEqualizer_Click(object sender, EventArgs e)
        {
            openChildForm(new Form3());
            hideSubMenu();
        }

        private void btnPlay_Click(object sender, EventArgs e)
        {
            mp3Player.play();
        }
    }
}
