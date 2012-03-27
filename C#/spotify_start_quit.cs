using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.Diagnostics;
using System.Threading;


class check_spotify

{
        // Fields

        private const uint EVENT_OBJECT_CREATE = 0x00008000;
        private const uint EVENT_OBJECT_DESTROY = 0x00008001;
        private const uint WINEVENT_OUTOFCONTEXT = 0;
        private const uint EVENT_OBJECT_NAMECHANGE = 0x800c;
        public static IntPtr new_hwnd = IntPtr.Zero;
        public check_spotify()
        {
                new_hwnd = getspotify();

        }

        // Methods
        [DllImport("user32.dll", SetLastError=true)]
                internal static extern IntPtr FindWindow(string lpClassName, string lpWindowName);
        [DllImport("user32")]
                internal static extern  bool GetMessage(ref Message lpMsg, IntPtr handle, uint mMsgFilterInMain, uint mMsgFilterMax);


        [DllImport("user32.dll")]
                private static extern IntPtr SetWinEventHook(uint eventMin, uint eventMax, IntPtr hmodWinEventProc, 
                                WinEventDelegate lpfnWinEventProc, uint idProcess, uint idThread, uint dwFlags);

        [DllImport("user32.dll")]
                private static extern bool UnhookWinEvent(IntPtr hWinEventHook);


        [DllImport("user32.dll", CharSet=CharSet.Auto, SetLastError=true)]
                internal static extern int GetWindowText(IntPtr hWnd, StringBuilder lpString, int nMaxCount);

        [DllImport("user32.dll", CharSet=CharSet.Auto, SetLastError=true)]
                internal static extern int GetWindowTextLength(IntPtr hWnd);

        [DllImport("user32")]
                internal static extern int GetWindowThreadProcessId(IntPtr hWnd, out int processId);

        private static WinEventDelegate procDelegate = new WinEventDelegate(check_spotify.WinEventProc);

        private delegate void WinEventDelegate(IntPtr hWinEventHook, uint eventType, IntPtr hwnd, int idObject, int 
                        idChild, uint dwEventThread, uint dwmsEventTime);




        private static void WinEventProc(IntPtr hWinEventHook, uint eventType, IntPtr hwnd, int idObject, int idChild, uint 
                        dwEventThread, uint dwmsEventTime)
        {

                if (idObject == 0 && idChild==0)
                {
                        if(hwnd.ToInt32() == getspotify().ToInt32())
                        {
                                if(eventType == EVENT_OBJECT_CREATE)
                                {
                                        Console.WriteLine("inside create"); 
                                        new_hwnd = getspotify();
                                }

                        }


                        else if(hwnd.ToInt32()==new_hwnd.ToInt32())
                        {

                                if(eventType == EVENT_OBJECT_DESTROY)
                                        Console.WriteLine("inside destroy"); 

                        }
                }

        }




        public int getprocessid(IntPtr hwnd)
        {
                int processId = 0;
                int windowThreadProcessId = GetWindowThreadProcessId(hwnd, out processId);
                return processId;
        }

        public static IntPtr getspotify()
        {
                return FindWindow("SpotifyMainWindow", null);
        }




        public static void Main()
        {
                check_spotify tracker = new check_spotify();
                IntPtr hwnd = getspotify();
                int num = tracker.getprocessid();
                IntPtr hWinEventHook = SetWinEventHook(0x00008000,0x00008001,IntPtr.Zero, procDelegate, 0, 0, 0);

                Message msg = new Message();

                while(GetMessage(ref msg,hwnd,0,0))

                        UnhookWinEvent(hWinEventHook);
        }


}






