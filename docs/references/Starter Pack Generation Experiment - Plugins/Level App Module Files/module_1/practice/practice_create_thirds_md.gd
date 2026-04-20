extends SequenceEvent

func trigger() -> void:
	var frac_bar := get_frac_shape()
	use_cut_hint_tool(frac_bar, 1, 3)
	use_cut_hint_tool(frac_bar, 2, 3)