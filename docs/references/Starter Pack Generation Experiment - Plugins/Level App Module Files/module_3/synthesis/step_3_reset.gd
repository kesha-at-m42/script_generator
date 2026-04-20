extends SequenceEvent

func trigger():
	clear_highlights(get_frac_bar())
	clear_highlights(get_frac_bar(1))