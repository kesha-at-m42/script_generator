extends SequenceEvent

func trigger() -> void:
	var line = get_number_line()
	for tick in line._ticks:
		if !tick.is_frac_label_visible:
			tick.is_frac_label_visible = true
			await delay(0.5)
	line._ticks[line._ticks.size()-1].numerator = 6
	line._ticks[line._ticks.size()-1].denominator = 1
