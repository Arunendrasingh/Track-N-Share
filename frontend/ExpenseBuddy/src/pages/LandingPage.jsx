// LandingPage.js
import React from 'react';
import {
    Box, Button, Container, Heading, Text, Stack, useBreakpointValue, Flex, Icon,
    Input,
    Avatar,
    IconButton,
    SimpleGrid,
} from '@chakra-ui/react';

import { FaBell, FaChartPie, FaDollarSign, FaWallet } from "react-icons/fa";

const LandingPage = () => {
    //   const headingSize = useBreakpointValue({ base: '2xl', md: '4xl' });

    return (
        <Box>
            {/* Header */}
            <Box bg="green.500" color="white" p={4} textAlign="center">
                <Heading as="h1" size="xl">Track-N-Share</Heading>
            </Box>

            {/* Hero Section */}
            <Box bg="white" borderRadius="md" boxShadow="md" p={8} m={4}>
                <Heading as="h2" size="xl" textAlign="center">
                    Welcome to Track-N-Share
                </Heading>
                <Text textAlign="center" mt={4}>
                    Your ultimate expense tracking and management tool. Easily track your
                    expenses, set monthly budgets, and share costs with friends and family.
                </Text>
                <Button colorScheme="green" mt={4} size="lg" onClick={() => window.location.href = '/dashboard.html'}>
                    Get Started
                </Button>
            </Box>

            {/* Features Section */}
            <Flex justifyContent="space-between" flexWrap="wrap" m={4}>
                <Box bg="white" borderRadius="md" boxShadow="md" p={4} m={2} flex={1} minWidth="200px">
                    <Heading as="h3" size="md" textAlign="center">Track Expenses</Heading>
                    <Text textAlign="center" mt={2}>
                        Monitor your daily expenses with ease and get insights into your spending habits.
                    </Text>
                </Box>
                <Box bg="white" borderRadius="md" boxShadow="md" p={4} m={2} flex={1} minWidth="200px">
                    <Heading as="h3" size="md" textAlign="center">Set Budgets</Heading>
                    <Text textAlign="center" mt={2}>
                        Set monthly budgets and track how well you're sticking to them.
                    </Text>
                </Box>
                <Box bg="white" borderRadius="md" boxShadow="md" p={4} m={2} flex={1} minWidth="200px">
                    <Heading as="h3" size="md" textAlign="center">Share Costs</Heading>
                    <Text textAlign="center" mt={2}>
                        Easily split expenses with friends and family, and manage group spending.
                    </Text>
                </Box>
            </Flex>

            {/* Footer */}
            <Box bg="green.500" color="white" p={2} textAlign="center">
                <Text>&copy; 2024 Track-N-Share. All rights reserved.</Text>
            </Box>
        </Box>
    );
};





function Dashboard() {
    return (
        <Flex h="100vh" bg="gray.100">
            {/* Sidebar */}
            <Box w="250px" bg="gray.900" color="white" p={4}>
                <Flex direction="column" gap={4}>
                    <Box>
                        <Text fontSize="2xl" fontWeight="bold">
                            Dashboard
                        </Text>
                    </Box>
                    <Flex direction="column" gap={2}>
                        <Flex align="center" p={2} borderRadius="md" _hover={{ bg: "gray.700" }}>
                            <Icon as={FaChartPie} mr={2} />
                            <Text>Overview</Text>
                        </Flex>
                        <Flex align="center" p={2} borderRadius="md" _hover={{ bg: "gray.700" }}>
                            <Icon as={FaDollarSign} mr={2} />
                            <Text>Expenses</Text>
                        </Flex>
                        <Flex align="center" p={2} borderRadius="md" _hover={{ bg: "gray.700" }}>
                            <Icon as={FaWallet} mr={2} />
                            <Text>Wallets</Text>
                        </Flex>
                    </Flex>
                </Flex>
            </Box>

            {/* Main Content */}
            <Flex direction="column" flex="1" p={4}>
                {/* Top Navigation */}
                <Flex justify="space-between" mb={6}>
                    <Input placeholder="Search..." w="300px" />
                    <Flex align="center">
                        <IconButton icon={<FaBell />} variant="ghost" mr={4} />
                        <Avatar name="John Doe" />
                    </Flex>
                </Flex>

                {/* Dashboard Cards */}
                <SimpleGrid columns={[1, null, 3]} spacing="20px" mb={6}>
                    <Box bg="white" p={4} borderRadius="md" shadow="sm">
                        <Heading size="md" mb={2}>
                            Total Expenses
                        </Heading>
                        <Flex align="center">
                            <Icon as={FaDollarSign} boxSize={8} mr={2} />
                            <Text fontSize="2xl" fontWeight="bold">
                                $1200
                            </Text>
                        </Flex>
                    </Box>
                    <Box bg="white" p={4} borderRadius="md" shadow="sm">
                        <Heading size="md" mb={2}>
                            Total Income
                        </Heading>
                        <Flex align="center">
                            <Icon as={FaWallet} boxSize={8} mr={2} />
                            <Text fontSize="2xl" fontWeight="bold">
                                $3000
                            </Text>
                        </Flex>
                    </Box>
                    <Box bg="white" p={4} borderRadius="md" shadow="sm">
                        <Heading size="md" mb={2}>
                            Savings
                        </Heading>
                        <Flex align="center">
                            <Icon as={FaChartPie} boxSize={8} mr={2} />
                            <Text fontSize="2xl" fontWeight="bold">
                                $1800
                            </Text>
                        </Flex>
                    </Box>
                </SimpleGrid>

                {/* Placeholder for Charts */}
                <Box bg="white" p={4} borderRadius="md" shadow="sm">
                    <Heading size="md" mb={2}>
                        Expense Chart
                    </Heading>
                    <Box h="300px">
                        {/* Insert chart component here */}
                    </Box>
                </Box>
            </Flex>
        </Flex>
    );
}

export default Dashboard;
