extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape()
	reset_cuts(frac_bar)
	use_cut_tool(frac_bar, 1, 2)