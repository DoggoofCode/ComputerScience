import streamlit as st
import numpy as np

class TitlePage:
    @classmethod
    def run(cls):
        pass

class SingleSolver:
    @classmethod
    def run(cls):
        pass

class GeneralSolver:
    @classmethod
    def run(cls):
        pass

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