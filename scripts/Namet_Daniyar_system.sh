#!/bin/bash

echo "=============================="
echo "Student Information"
echo "=============================="

echo "Name: Daniyar"
echo "Surname: Namet"
echo "Group: IT2-2312 SE"
echo "Student ID: 37056"

echo ""
echo "=============================="
echo "System Information"
echo "=============================="

echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -a)"

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "=============================="
echo "File Verification"
echo "=============================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

if [ -f "$PROJECT_DIR/Namet_Daniyar_info.txt" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
