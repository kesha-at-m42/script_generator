extends SequenceEvent

func trigger() -> void:
	clear_selected()
	clear_shaded(get_frac_shape(0))
	clear_shaded(get_frac_shape(1))
	clear_shaded(get_frac_shape(2))
	clear_shaded(get_frac_shape(3))
	clear_shaded(get_frac_shape(4))
