
import time

def ft_progress(lst):
    total = len(lst)
    #len of the bar
    progress_large = 40

    def show_progress(iteration):
        progress = int(progress_large * iteration / total)
        bar = f"[{'#' * progress}{'.' * (progress_large - progress)}] {iteration}/{total}"
        print(bar, end='\r')

    for i, item in enumerate(lst):
        yield item
        show_progress(i + 1)

if __name__ == "__main__":
    my_list = range(100)
    for number in ft_progress(my_list):
        # Simulation d'un traitement
        time.sleep(0.05)




