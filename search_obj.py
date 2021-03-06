#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from progressbar import *


class SearchNames():
    def __init__(self, bucket_names, num_buckets, threads, print_bucket_names, output_file):
        self.bucket_names = bucket_names
        self.num_buckets = num_buckets
        self.threads = threads
        self.print_bucket_names = print_bucket_names
        self.output_file = output_file
        self.progress = ProgressBar(num_buckets)


class SearchStrings():
    def __init__(self, num_chars, num_chars_range, string_options, threads, print_bucket_names, output_file, start_after_value, stop_at_value, prefix_postfix_option):
        self.num_chars = num_chars
        self.num_chars_range = num_chars_range
        self.string_options = string_options
        self.threads = threads
        self.print_bucket_names = print_bucket_names
        self.output_file = output_file
        self.start_after_value = start_after_value
        self.stop_at_value = stop_at_value
        self.prefix_postfix_option = prefix_postfix_option
