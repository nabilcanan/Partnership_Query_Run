import tkinter as tk
import tkinter.ttk as ttk
from creation_queries import new_function_creation
from neotech_queries import new_function_neotech
from jabil_queries import new_function_jabil
from sanmina_queries import new_function_sanmina
from benchmark_queries import new_function_benchmark
from SMTC_queries import new_function_smtc
from booking_report_query import new_function_booking


def gui_create(main_window):
    style = ttk.Style()
    main_window.configure(bg="white")
    # Adjusting button size and font size
    style.configure("TButton", font=("Roboto", 12, "bold"), width=30, height=2)
    style.map("TButton", foreground=[('active', 'white')], background=[('active', '#007BFF')])

    title_label = ttk.Label(main_window, text="Welcome Partnership Team!",
                            font=("Segoe UI", 24, "underline"), background="white", foreground="#103d81")
    title_label.pack(pady=10)  # Reduced padding

    description_label = ttk.Label(main_window,
                                  text="This tool allows you to run the Award, Backlog, Sales History,\n"
                                       "VPC and SND Queries for all of our Customers along with\n"
                                       "the booking report query.",
                                  font=("Roboto", 14), background="white", anchor="center",
                                  justify="center")
    description_label.pack(pady=10)  # Reduced padding

    # Creating buttons with less vertical padding
    run_creation_queries_button = ttk.Button(main_window, text="Run all 5 Creation Queries",
                                             command=new_function_creation, style="TButton")
    run_creation_queries_button.pack(pady=10)

    run_neotech_queries_button = ttk.Button(main_window, text="Run all 5 Neotech Queries",
                                            command=new_function_neotech, style="TButton")
    run_neotech_queries_button.pack(pady=10)

    run_jabil_queries_button = ttk.Button(main_window, text="Run all 5 Jabil Queries",
                                          command=new_function_jabil, style="TButton")
    run_jabil_queries_button.pack(pady=10)

    run_sanmina_queries_button = ttk.Button(main_window, text="Run all 5 Sanmina Queries",
                                            command=new_function_sanmina, style="TButton")
    run_sanmina_queries_button.pack(pady=10)

    run_benchmark_queries_button = ttk.Button(main_window, text="Run all 5 Benchmark Queries",
                                              command=new_function_benchmark, style="TButton")
    run_benchmark_queries_button.pack(pady=10)

    run_smtc_queries_button = ttk.Button(main_window, text="Run all 5 SMTC Queries",
                                         command=new_function_smtc, style="TButton")
    run_smtc_queries_button.pack(pady=10)

    run_booking_query_button = ttk.Button(main_window, text="Run Booking Report Query",
                                          command=new_function_booking, style="TButton")
    run_booking_query_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Query Running Program :)')
    root.geometry('600x550')
    gui_create(root)
    root.mainloop()
