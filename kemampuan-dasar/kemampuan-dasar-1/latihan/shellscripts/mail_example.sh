#!/bin/bash
Recipient="ahmadzaidi1994@gmail.com"
Subject="Salam Hangat"
Message="Selamat datang di rumah Uya"
	`mail -s $Subject $Recipient <<< $Message`
