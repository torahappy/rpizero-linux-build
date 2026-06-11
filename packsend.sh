#/bin/bash

set -e

. ./names.sh

MY_KERNEL_VERSION=$(cat build/include/config/kernel.release)

echo "Unpacking kernel..."
scp install.tar.xz $MYUSERNAME@$MYHOSTNAME:/home/$MYUSERNAME
ssh $MYUSERNAME@$MYHOSTNAME "cd /; sudo tar -xvf /home/$MYUSERNAME/install.tar.xz"

echo "Copying kernel config..."
scp './build/.config' $MYUSERNAME@$MYHOSTNAME:kernel-config
ssh $MYUSERNAME@$MYHOSTNAME "sudo cp /home/$MYUSERNAME/kernel-config /boot/config-$MY_KERNEL_VERSION"

echo "Creating initramfs..."
ssh $MYUSERNAME@$MYHOSTNAME "sudo /usr/sbin/mkinitramfs -o initramfs $MY_KERNEL_VERSION"
ssh $MYUSERNAME@$MYHOSTNAME "sudo cp initramfs /boot/firmware/initramfs-$MY_KERNEL_SUFFIX"

echo "Cleaning up..."
ssh $MYUSERNAME@$MYHOSTNAME "sudo rm initramfs install.tar.xz kernel-config"

echo "Rebooting..."
ssh $MYUSERNAME@$MYHOSTNAME "sudo reboot"
