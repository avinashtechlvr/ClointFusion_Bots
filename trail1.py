import ClointFusion as cf
import time

def login_wp(username="",password=""):
    cf.launch_website_h("https://tech2everyone.live/wp-admin/")
    cf.browser_write_h(username,"Username")
    cf.browser_write_h(password,"Password")
    cf.browser_mouse_click_h("Log In")
    cf.browser_mouse_click_h("Posts")
   
    lastpage= cf.browser_locate_element_h('//*[@id="posts-filter"]/div[1]/div[3]/span[2]/a[2]')
    cf.browser_mouse_click_h(lastpage)
    
    select_files = cf.browser_locate_element_h('//*[@id="cb-select-all-1"]')
    cf.browser_mouse_click_h(select_files)

    bulkaction = cf.browser_locate_element_h('//*[@id="bulk-action-selector-top"]')
    cf.browser_mouse_click_h(bulkaction)

    cf.key_press("down+down")
    cf.key_press("down+down")
    cf.key_hit_enter()

    Apply = cf.browser_locate_element_h('//*[@id="doaction"]')
    cf.browser_mouse_click_h(Apply)    

    cf.browser_quit_h()
    

password_file = open("wpbot/Password.txt","r")
Password = password_file.read()

login_wp("avinashch", Password)

cf.create_batch_file(application_exe_pyw_file_path=r"C:\Users\Avinash Chodavarapu\Desktop\Bots\wpbot\trail1.pyw.py")
cf.schedule_create_task_windows(Weekly_Daily="D",start_time_hh_mm_24_hr_frmt="13:13")

