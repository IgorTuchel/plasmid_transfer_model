def main():
    print("Select simulation type:")
    print("1 - ODE model")
    print("2 - SSA model")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        from ode_model import model, charts
        
        p = model.base_params.copy()
        beta_crit = model.get_beta_crit(p)
        s_crit = model.get_s_crit(p)

        print("\nAnalytical thresholds (base parameters):")
        print(f"Critical β = {beta_crit:.4f}")
        print(f"Critical s = {s_crit:.4f}\n")

        ts_results = model.run_time_series()
        charts.plot_time_series(ts_results)

        heatmap, beta_values, cost_values, beta_sweep, pf_sweep = model.run_beta_sweep()
        charts.plot_beta_heatmap(heatmap, beta_values, cost_values, beta_sweep, pf_sweep)

    elif choice == '2':
        from ssa_model import model, charts

        results = model.run_multiple_ssa()
        charts.plot_ssa_trajectories(results)
        
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()