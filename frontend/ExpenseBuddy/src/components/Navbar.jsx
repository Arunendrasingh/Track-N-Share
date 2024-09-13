import React from 'react';
import { Flex, IconButton, VStack, HStack, useBreakpointValue, Box } from "@chakra-ui/react";
import { FaHome, FaChartBar, FaUser, FaWallet } from "react-icons/fa";

const Navbar = () => {
  const isMobile = useBreakpointValue({ base: true, md: false });

  const navItems = [
    { icon: FaHome, label: 'Home' },
    { icon: FaWallet, label: 'Transactions' },
    { icon: FaUser, label: 'Profile' },
    { icon: FaChartBar, label: 'Stats' },
  ];

  return (
    <Flex
      direction={isMobile ? "row" : "column"}
      position="sticky"
      bottom={isMobile ? 0 : "auto"}
      left={isMobile ? "auto" : 0}
      h={isMobile ? "60px" : "100vh"}
      w={isMobile ? "100%" : "60px"}
      bg="gray.800"
      justifyContent="center"
      alignItems="center"
      p={2}
      zIndex="1000"
    >
      {isMobile ? (
        <HStack justify="space-around" w="100%">
          {navItems.map((item, index) => (
            <IconButton
              key={index}
              icon={<item.icon />}
              aria-label={item.label}
              variant="ghost"
              color="white"
              size="lg"
            />
          ))}
        </HStack>
      ) : (
        <VStack spacing={4}>
          {navItems.map((item, index) => (
            <IconButton
              key={index}
              icon={<item.icon />}
              aria-label={item.label}
              variant="ghost"
              color="white"
              size="lg"
            />
          ))}
        </VStack>
      )}
    </Flex>
  );
};

export default Navbar;