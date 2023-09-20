from matplotlib import pyplot as plt

class Analysis:
    def _init_(self, x, y):
        self.PltNames = []
        self.Input_Files = []
        self.List_Of_Coordinates = []
        self.Colour_key = {0: ["Black", "Grey", "Silver"],
                           1: ["Maroon", "Orange", "Salmon"],
                           2: ["Navy", "RoyalBlue", "SkyBlue"],
                           3: ["Green", "LimeGreen", "LightGreen"],
                           4: ["Magenta", "Violet", "Thistle"],
                           5: ["Peru", "SandyBrown", "Wheat"]}

        self.X_Title = x
        self.Y_Title = y
        self.Uncertainty_Name_One = ""
        self.Uncertainty_Name_Two = ""

    def add_file(self, input_file_name, plt_name):
        self.Input_Files.append(input_file_name)
        self.PltNames.append(plt_name)

    def update_lists(self, granularity=24, start_row=0, stop_row=2048, u_n_1= "Bias uncertainty",
                     u_n_2="Measuring and sampling uncertainty"):
        self.Uncertainty_Name_One = u_n_1
        self.Uncertainty_Name_Two_ = u_n_2
        x_column = 0
        y_column = 1
        y_error_upper_first_type = 2
        y_error_lower_first_type = 3
        y_error_upper_second_type = 4
        y_error_lower_second_type = 5

        for i in self.Input_Files:
            f = open(i, 'r')
            x_int = []
            y_int = []
            y_error_upper_first_int = []
            y_error_lower_first_int = []
            y_error_upper_second_int = []
            y_error_lower_second_int = []

            for big_data in f.readlines():
                data = big_data.split(',')
                x_int.append(data[x_column])
                y_int.append(data[y_column])
                y_error_upper_first_int.append(data[y_error_upper_first_type])
                y_error_lower_first_int.append(data[y_error_lower_first_type])
                y_error_upper_second_int.append(data[y_error_upper_second_type])
                y_error_lower_second_int.append(data[y_error_lower_second_type])
            average_x = []
            average_y = []
            average_y_upper_first_error = []
            average_y_lower_first_error = []
            average_y_upper_second_error = []
            average_y_lower_second_error = []
            cumulative_data = 0
            list_in_use = []

            for count in range(6):
                if count == 0:
                    list_in_use = x_int
                    average_list_in_use = average_x
                elif count == 1:
                    list_in_use = y_int
                    average_list_in_use = average_y
                elif count == 2:
                    list_in_use = y_error_upper_first_int
                    average_list_in_use = average_y_upper_first_error
                elif count == 3:
                    list_in_use = y_error_lower_first_int
                    average_list_in_use = average_y_lower_first_error
                elif count == 4:
                    list_in_use = y_error_upper_second_int
                    average_list_in_use = average_y_upper_second_error
                elif count == 5:
                    list_in_use = y_error_lower_second_int
                    average_list_in_use = average_y_lower_second_error
                for list_index in range(len(list_in_use)):
                    if (start_row + list_index) == stop_row:
                        break
                        cumulative_data = 0

                if count == 0:
                    average_x = average_list_in_use

                elif count == 1:
                    average_y = average_list_in_use
                elif count == 2:
                    average_y_upper_first_error = average_list_in_use
                elif count == 3:
                    average_y_lower_first_error = average_list_in_use
                elif count == 4:
                    average_y_upper_second_error = average_list_in_use
                elif count == 5:
                    average_y_lower_second_error = average_list_in_use
                cumulative_data = 0
            sel.List_of_Coordinates.append(list(zip(average_x, average_y, average_y_upper_first_error,
                                           average_y_lower_first_error, average_y_upper_second_error,
                                           average_y_lower_second_error)))

    def plot_with_errors(self, amount_of_errors, index, colour=0):
        year = []
        ly_average = []
        ly_upper_one = []
        ly_lower_one = []
        ly_upper_two = []
        ly_lower_two = []
        list_of_this_files_coordinates = self.List_of_Coordinates[index]
        for j in range (len(list_of_this_files_coordinates)):
            raw_data = list_of_this_files_coordinates[j]
            year.append(raw_data[0])
            ly_average.append(raw_data[1])
            ly_upper_one.append(raw_data[2])
            ly_lower_one.append(raw_data[3])
            ly_upper_two.append(raw_data[4])
            ly_lower_two.append(raw_data[5])

        plt.title("Nomial plots")
        plt.xlabel(self.X_Title)
        plt.ylabel(self.Y_Title)
        # needs to change so user can select a colour^
        colour_list = self.Colour_key[colour]
        plt.plot(year, ly_average, color=colour_list[0], label=self.PltNames[index])
        if ly_upper_one[0] - ly_upper_two[0] < 0:
            if amount_of_errors == 1 or amount_of_errors == 2:
                plt.fill_between(year, ly_upper_one, ly_lower_one, color=colour_list[2],
                                   label=self.Uncertainty_Name_One)
            if amount_of_errors == 2:
                plt.fill_between(year, ly_upper_two, ly_lower_two, color=colour_list[1],
                                   label=self.Uncertainty_Name_Two)
        elif ly_upper_one[0] - ly_upper_two[0] > 0:
            if amount_of_errors == 1 or amount_of_errors == 2:
                plt.fill_between(year, ly_upper_two, ly_lower_two, color=colour_list[2],
                                   label=self.Uncertainty_Name_Two)
            if amount_of_errors == 2:
                plt.fill_between(year, ly_upper_one, ly_lower_one, color=colour_list[1],
                                   label=self.Uncertainty_Name_One)
        plt.legend()

    def scatter_plot(self, data_set_one, data_set_two, data_set_colour_one, data_set_colour_two):
        first_plot = self.List_of_Coordinates[data_set_one]
        first_plot_name = self.PltNames[data_set_one]
        second_plot = self.List_of_Coordinates[data_set_two]
        second_plot_name = self.PltNames[data_set_two]
        colour_list_one = self.Colour_key[data_set_colour_one]
        colour_list_two = self.Colour_key[data_set_colour_two]
        first_plot_y = []
        second_plot_y = []
        plot_x = []

        for i in range (len(first_plot)):
            first_plot_tuple=first_plot[i]
            second_plot_tuple=second_plot[i]
            first_plot_y.append(first_plot_tuple[1])
            second_plot_y.append(second_plot_tuple[1])
            plot_x.append(first_plot_tuple[0])
        plt.scatter(plot_x, first_plot_y, color=colour_list_one[0], label=first_plot_name)
        plt.scatter(plot_x, second_plot_y, color=colour_list_two[0], label=second_plot_name)
        plt.legend()

    def clearlist(self):
        self.List_of_Coordinates = []









