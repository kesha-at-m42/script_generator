extends SequenceEvent

func trigger():
	for index in range(4):
		await play_count_up_animation(get_frac_bar(index))
		await delay(0.2)