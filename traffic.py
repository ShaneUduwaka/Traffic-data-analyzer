#Author : D.S.S Uduwaka
#Date : 11 / 19 / 2024
#Student ID : 20231839 / w2120183

from graphics import *     #Importing all the functions in the graphics library to create the Histrogram.

#Task A : Input Validation

def validate_date_():

        """
        Prompts the user for a date in DD MM YYYY format, validates the input for:
        - Correct data type
        - Correct range for day, month, and year
        """
        
        global file_name       #Made the variable global because other functions need to access the value in it.
        
        file_name = ''      
        day = 0
        mon = 0
        yr = 0

        print('\n')
           
        while True:                      
            try:               
                day = str(input('Please enter the day of the survey in the format dd: '))
                if int(day) > 31 or int(day) < 1:
                        print('Out of range - value must be in the range 1 to 31.')
                elif len(day)== 1:
                        print('Value must be in the format DD')          #checks for the correct format
                else:
                        break
            except ValueError:
                print('Integer required')
        
        
        while True:                        
            try:            
                mon = str(input('Please enter the month of the survey in the format MM: '))
                if int(mon) > 12 or int(mon) < 1:
                        print('Out of range - value must be in the range 1 to 12.')
                elif len(mon)== 1:
                        print('Value must be in the format MM')                        
                else:
                        break
            except ValueError:           
                print('Integer required')

        
        while True:           
            try:
                yr = str(input('Please enter the year of the survey in the format YYYY: '))
                if int(yr) < 2000 or int(yr) > 2024:
                        print('Out of range - value must lie in the range 2000 to 2024.')
                else:
                        break
            except ValueError:
                print('Integer required')
                
        file_name = day + mon + yr              #(day+month+yr) added to a string called file_name to access data. 
        
        print('\n')

 
#Task B : Processed Outcomes


def process_csv_data(file_name):
        
        """
        Processes the CSV data for the selected date and extracts:
        - Total vehicles
        - Total trucks
        - Total electric vehicles
        - Two-wheeled vehicles, and other requested metrics
        """
        global outcomes

        outcomes = []  #All outcomes will be appended to this list.
                
        def process_csv_data():

                global Elm_vehicles_per_hour
                global hours24
                global hanley_vehicles_per_hour
                             
                f1 = open('traffic_data' + file_name + '.csv','r')

                #Initializing Variables
                
                all_info = []
                totalvehicles = []
                totaltrucks = []
                elmSpeedLimit = []
                hanleySpeedLimit = []
                elm_allvehicles = []
                all_vehi_in_day_Elm = []
                all_vehi_in_day_hanley = [] #The recorded hour of a vehicle passing through the Hanley Highway/Westway throughout the day.
                hours24 = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23'] #24 hours in a day acsending order.
                hanley_vehicles_per_hour = []    #vehicles per hour in a day in Hanley Highway/Westway.
                Elm_vehicles_per_hour = []     #vehicles per hour in a day in Elm Avenue/Rabbit Road. 
                index_of_max = 0        #index of the most vehicles in a hour value.
                rain = []
                
                #reading the data in csv file to a list.
                #PyLenin (2018) How to read CSV files with Python #1 - Without using python libraries.
                #Reference Available at: https://www.youtube.com/watch?v=GBD4na8AQjY&t=1s

                for row in f1:        
                        all_info.append((row.strip()).split(','))
                        
                del all_info[0]         #Deleting the header row.

                #Logic for processing data goes here.
                
                #Use of list comprehension with formatted strings.
                
                outcomes.append(f"The total number of vehicles recorded for this date is {len(all_info)}")
                outcomes.append(f"The total number of trucks recorded for this date is {len([x for x in all_info if x[8]== 'Truck'])}")             
                outcomes.append(f"The total number of electric vehicles for this date is {len([x for x in all_info if x[9]== 'True'])}")                                                              
                outcomes.append(f"The total number of two-wheeled vehicles for this date is {len([x for x in all_info if x[8]=='Motorcycle' or x[8]=='Bicycle' or x [8]=='Scooter'])}")      
                outcomes.append(f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {len([x for x in all_info if x[0]=='Elm Avenue/Rabbit Road' and x[4]=='N' and x[8]=='Buss'])}")
                outcomes.append(f"The total number of Vehicles through both junctions not turning left or right is {len([x for x in all_info if x[3]==x[4]])}")

                totalvehicles = len(all_info)
                totaltrucks = len([x for x in all_info if x[8]== 'Truck'])
                outcomes.append(f"The percentage of total vehicles recorded that are trucks for this date is {round(totaltrucks / totalvehicles * 100)}%")
                
                outcomes.append(f"the average number of Bikes per hour for this date is {round((len([x for x in all_info if x[8]== 'Bicycle'])) / 24) }")

                elmSpeedLimit = len([x for x in all_info if x[0]== 'Elm Avenue/Rabbit Road' and int(x[7]) > 30])
                hanleySpeedLimit = len([x for x in all_info if x[0]== 'Hanley Highway/Westway' and int(x[7]) > 20])
                outcomes.append(f"\nThe total number of Vehicles recorded as over the speed limit for this date is {elmSpeedLimit + hanleySpeedLimit}")

                elm_allvehicles = len([x for x in all_info if x[0]== 'Elm Avenue/Rabbit Road'])
                outcomes.append(f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {elm_allvehicles}")

                outcomes.append(f"The total number of vehicles recorded through Hanley Highway/Westway junction is {len([x for x in all_info if x[0]== 'Hanley Highway/Westway'])}")
           
                outcomes.append(f"{int((len([x for x in all_info if x[8]== 'Scooter' and x[0]== 'Elm Avenue/Rabbit Road'])) / elm_allvehicles * 100) }% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.")

                all_vehi_in_day_hanley = [x[2].split(':')[0] for x in all_info if x[0]== 'Hanley Highway/Westway']                  
                hanley_vehicles_per_hour = [all_vehi_in_day_hanley.count(x) for x in hours24] 
                outcomes.append(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {max(hanley_vehicles_per_hour)}")

                index_of_max = hanley_vehicles_per_hour.index(max(hanley_vehicles_per_hour))
                outcomes.append(f"The most vehicles through Hanley Highway/Westway were recorded between {hours24[index_of_max]}.00 and {int(hours24[index_of_max])+1}.00")

                rain = [x[2].split(':')[0] for x in all_info if x[5]== 'Heavy Rain' or x[5]=='Light Rain']
                outcomes.append(f"The number of hours of rain for this date is {len(set(rain))}")
               
                all_vehi_in_day_Elm = [x[2].split(':')[0] for x in all_info if x[0]== 'Elm Avenue/Rabbit Road'] #The two lists here are used for Task D.
                Elm_vehicles_per_hour = [all_vehi_in_day_Elm.count(x) for x in hours24] 
                
                f1.close()

        def display_outcomes():

                """
                Displays the calculated outcomes in a clear and formatted way.
                """
                
                print('\n************************************')
                print('data file selected is','traffic_data' + file_name + '.csv')
                print('************************************')
                for i in range(0,15):                 #Printing outcomes to the console.
                        print(outcomes[i])
                print('\n************************************')

        global no_file
        no_file = None
        
        try:          
                f1 = open('traffic_data' + file_name + '.csv','r')
                process_csv_data()
                display_outcomes()
                no_file = False
                

        except FileNotFoundError:     #if the file does not exist in directory.
                print('No such file or directory :','\'traffic_data' + file_name + '.csv\'')
                no_file = True
                
                

# Task C: Save Results to Text File


def save_results_to_file(outcomes):

        """
        Saves the processed outcomes to a text file and appends if the program loops.
        """
        
        if no_file == False:
                
                with open("results.txt",'a') as file:
                
                        file.write('data file selected is' + ' traffic_data' + file_name + '.csv\n')              
                        for outs in outcomes:
                                file.write(outs + '\n')
                                
                        file.write('\n************************************\n')


# Task D: Histogram Display


class HistogramApp:

        window = None

        def __init__(self,date,hours,elmcount,hancount):

                """
                Initializes the histogram application.
                """
                
                self.date = date
                self.hours24 = hours
                self.elmcount = elmcount
                self.hancount = hancount

        def setup_window(self):

                """
                Sets up the Graphics window.
                """

                self.window = GraphWin('Histrogram',1050,550)

        def draw_histogram(self):

                """
                Draws the histogram with axes, labels, and bars.
                """
             
                timetext = Text(Point(525,525),'Hours 00:00 to 24:00')
                timetext.setSize(9)
                timetext.setFace('helvetica')
                timetext.draw(self.window)

                count = 0
                greenscale = 0
                redscale = 0
                
                for i in range(0,936,39):

                        maxvalues = []  #getting the max value of the hours in a day
                        maxvalues.append(max(self.elmcount)) 
                        maxvalues.append(max(self.hancount))
                        
                        greenscale = (self.elmcount[count] / max(maxvalues)) * 300    #Scaling ensures codes usability to any given value per hour.    
                        
                        greenlegend = Rectangle(Point(57+i,465-greenscale),Point(74+i,465))   #Creating Green bars.
                        greenlegend.setFill(color_rgb(3, 252, 190))
                        greenlegend.draw(self.window)

                        greencount_text = Text(Point(65+i,(465-greenscale)-6),self.elmcount[count]) #Display the hourly count.
                        greencount_text.setStyle('bold')
                        greencount_text.setSize(7)
                        greencount_text.draw(self.window)

                        redscale = (self.hancount[count] / max(maxvalues)) * 300
                        
                        redlegend = Rectangle(Point(74+i,465-redscale),Point(91+i,465))       #Creating Red bars.
                        redlegend.setFill(color_rgb(252, 3, 111))
                        redlegend.draw(self.window)

                        redcount_text = Text(Point(82+i,(465-redscale)-6),self.hancount[count])
                        redcount_text.setStyle('bold')
                        redcount_text.setSize(7)
                        redcount_text.draw(self.window)

                        hourtext = Text(Point(74+i,477),self.hours24[count])
                        hourtext.setStyle('bold')
                        hourtext.setSize(8)                    #The hour under the bars.
                        hourtext.draw(self.window)

                        count += 1
                
                line = Line(Point(57,466),Point(989,466))
                line.draw(self.window)                          #The horizontal line under the bars.
            
        def add_legend(self):

                """
                Adds a legend to the histogram to indicate which bar corresponds to which junction.
                """

                #Creating the title above the legend.
                                                                               #String slicing to show the output in the given format.
                title = Text(Point(250,25),f"Histrogram of Vehicle Frequency per Hour  ({self.date[0:2]}/{self.date[2:4]}/{self.date[4:]})")
                title.setSize(11)
                title.setStyle('bold')
                title.setFace('helvetica')        #Changing the font.
                title.draw(self.window)

                #Creating the first legend.

                greenlegend = Rectangle(Point(57,45),Point(70,55))
                greenlegend.setFill(color_rgb(3, 252, 190))
                greenlegend.draw(self.window)
                             
                text1 = Text(Point(150,50),'Elm Avenue/Rabbit Road')
                text1.setSize(9)
                text1.setFace('helvetica')
                text1.draw(self.window)

                #Creating the Second legend.

                redlegend = Rectangle(Point(57,65),Point(70,75))
                redlegend.setFill(color_rgb(252, 3, 111))
                redlegend.draw(self.window)

                text2 = Text(Point(150,70),'Hanley Highway/Westway')
                text2.setSize(9)
                text2.setFace('helvetica')
                text2.draw(self.window)

                try:
                        self.window.getMouse()     #The window will pause until user clicks on the window.

                except GraphicsError:
                        pass

                self.window.close()

        def run(self):

                """
                Runs the Tkinter main loop to display the histogram.
                """

                self.setup_window()
                self.draw_histogram()
                self.add_legend()
                
      
# Task E: Code Loops to Handle Multiple CSV Files


class MultiCSVProcessor:

        def _init_(self):

                """
                Initializes the application for processing multiple CSV files.
                """

                self.currentdata = None

        def load_csv_file(self):

                """
                Loads a CSV file and processes its data.
                """

                validate_date_()
                process_csv_data(file_name)
                save_results_to_file(outcomes)

                if no_file == False:
                        
                        Histogram_Data = None            #The variable that will hold the object and values of that instance.
                        Histogram_Data = HistogramApp(file_name,hours24,Elm_vehicles_per_hour,hanley_vehicles_per_hour)
                        Histogram_Data.run()

                if no_file == True:
                        self.currentdata = None

                self.currentdata = True
               
        def clear_previous_data(self):

                """
                Clears data from the previous run to process a new dataset.
                """

                self.currentdata = None
                
        def handle_user_interaction(self):

                """
                Handles user input for processing multiple files.
                """

                validate_continue_input()

        def process_files(self):

                """
                Main loop for handling multiple CSV files until the user decides to quit.
                """
                while True:
                    
                    self.load_csv_file()
                    self.handle_user_interaction()

                    if yesNo == 'y':
                        continue

                    elif yesNo == 'n':
                        print('\nEnd of run')
                        break



def validate_continue_input():

        """
        Prompts the user to decide whether to select another data file for a different date:
        - Validates "Y" or "N" input
        """
        
        global yesNo

        yesNo = ''

        print('\n')
        
        while True:
                try:
                         yesNo = str(input('Do you want to select another data file for a different date? Y/N > ')).strip().lower()
                         
                         if yesNo != 'n' and yesNo != 'y':
                                 print('Please enter “Y” or “N”')            #The program will loop until the user prompt a validate input.                                                         
                         else:
                                 break       
                except ValueError:
                         print('Please enter “Y” or “N”')
              


# Main Program
                

program = MultiCSVProcessor()
program.process_files()



