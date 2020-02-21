#!/usr/bin/env bash
python caption.py --img data/img/Flicker8k_Dataset/3726629271_7639634703.jpg \
    --model BEST_checkpoint_flickr8k_5_cap_per_img_5_min_word_freq.pth.tar \
    --word_map data/output/WORDMAP_flickr8k_5_cap_per_img_5_min_word_freq.json \
    --beam_size 5