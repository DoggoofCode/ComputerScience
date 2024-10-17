import streamlit as st
import numpy as np

class TitlePage:
    @classmethod
    def run(cls):
        st.title("Trajectory Solver")
        st.write("---")
        st.write(
            "This project aims to help student calculate the trajectory"
            " of an object in a 2 dimensional plane, as well as finding"
            " the trajectories properties"
        )

class GeneralSolver:
    @classmethod
    def run(cls):
        pass

class SingleSolver:
    @classmethod
    def run(cls):
        def sin(x):
            return np.sin(x)
        def sin2(x):
            return np.sin(x)**2

        st.title("Trajectory Solver")
        #tabs
        max_height_tab, time_of_flight_tab, horizontal_range_tab = st.tabs(
            [
                "Max Height",
                "Time of Flight",
                "Horizontal Range"
             ]
        )

        equations = {
            "max_height_equation": lambda vel, theta, g_acc: (vel ** 2) * sin2(theta) / (2 * g_acc),
            "time_of_flight_equation": lambda vel, theta, g_acc: 2 * vel * sin(theta) / g_acc,
            "horizontal_range_equation": lambda vel, theta, g_acc: vel**2 * sin(2*theta) / g_acc
        }

        # I have chosen a 2dp. degree of accuracy for its commonality and simplicity
        a, b = st.columns(2)
        with a:
            rel_velocity = st.number_input(
                "Please input the release velocity(m/s)",
                key="release_velocity",
                help="This is the angle that one throws the ball at"
            )
        with b:
            rel_angle = st.number_input(
                "Please input the release angle (º)",
                key="release_angle",
                min_value=0.00,
                max_value=90.00,
                help="This is the angle that one throws the ball at"
            )

        grav_acc = st.number_input(
            "(Advanced) Input gravitational acceleration (m/s^2)",
            key="g_acceleration",
            min_value=0.00,
            value=9.8,
            help="This is the acceleration of gravity"
        )

        calculate_button = st.button("Calculate!", key="calculate button", icon="💻")

        with max_height_tab:
            name = "Maximum Height"
            val = equations["max_height_equation"](rel_velocity, rel_angle, grav_acc)
            unit = "metres"
            if calculate_button:
                st.markdown(
                    f"""
                    <div style="background-color: #ff4b4b; padding: 10px; border-radius: 5px;">
                        <h6 style="color: white;">The {name} is {round(val, 2)} {unit}</h6>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        with time_of_flight_tab:
            name = "Time of Flight"
            val = equations["time_of_flight_equation"](rel_velocity, rel_angle, grav_acc)
            unit = "seconds"
            if calculate_button:
                st.markdown(
                    f"""
                    <div style="background-color: #ff4b4b; padding: 10px; border-radius: 5px;">
                        <h6 style="color: white;">The {name} is {round(val, 2)} {unit}</h6>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        with horizontal_range_tab:
            name = "Horizontal Range"
            val = equations["horizontal_range_equation"](rel_velocity, rel_angle, grav_acc)
            unit = "metres"
            if calculate_button:
                st.markdown(
                    f"""
                    <div style="background-color: #ff4b4b; padding: 10px; border-radius: 5px;">
                        <h6 style="color: white;">The {name} is {round(val, 2)} {unit}</h6>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


def main():
    st.set_page_config(
        layout="wide",
        page_title="Trajectory Solver"
    )

    solver_mode = st.sidebar.selectbox(
        "",
        [
            "Title Screen",
            "General Solve",
            "Single Solve",
        ]
    )

    if solver_mode == "Title Screen":
        TitlePage.run()
    elif solver_mode == "General Solve":
        GeneralSolver.run()
    elif solver_mode == "Single Solve":
        SingleSolver.run()

if __name__ == '__main__':
    main()