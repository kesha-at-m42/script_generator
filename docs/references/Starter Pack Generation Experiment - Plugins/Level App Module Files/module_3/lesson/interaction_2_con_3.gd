extends SequenceEvent

func trigger() -> void:
	var bar = get_frac_shape()
	clear_highlights(bar)
	clear_labels(bar)
