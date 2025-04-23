import React from 'react';
import { ChakraProvider, Box, VStack, Heading, Text, Button, Container, useColorModeValue, Flex, Image, SimpleGrid, Stat, StatLabel, StatNumber, Icon } from '@chakra-ui/react';
import { FiTrendingUp, FiLock, FiDatabase } from 'react-icons/fi';

function App() {
  const bgColor = useColorModeValue('gray.50', 'gray.900');
  const statBg = useColorModeValue('white', 'gray.700');

  return (
    <ChakraProvider>
      <Box bg={bgColor} minH="100vh">
        {/* Hero Section */}
        <Container maxW="container.xl" pt={20}>
          <Flex direction={{ base: 'column', md: 'row' }} align="center" justify="space-between">
            <VStack align="start" spacing={6} maxW="600px">
              <Heading as="h1" size="2xl" bgGradient="linear(to-r, blue.400, purple.500)" bgClip="text">
                SEMD Token
              </Heading>
              <Text fontSize="xl" color="gray.600">
                המטבע המתקדם ביותר על רשת סולנה המשלב בינה מלאכותית, מסחר אוטומטי ואנליטיקה מתקדמת
              </Text>
              <Button
                size="lg"
                colorScheme="purple"
                bgGradient="linear(to-r, blue.400, purple.500)"
                _hover={{
                  bgGradient: 'linear(to-r, blue.500, purple.600)',
                }}
              >
                התחל לסחור
              </Button>
            </VStack>
            <Box boxSize={{ base: '300px', md: '500px' }} mt={{ base: 10, md: 0 }}>
              <Image src="/token-3d.png" alt="SEMD Token" />
            </Box>
          </Flex>
        </Container>

        {/* Stats Section */}
        <Container maxW="container.xl" py={20}>
          <SimpleGrid columns={{ base: 1, md: 3 }} spacing={10}>
            <Stat bg={statBg} p={6} rounded="lg" shadow="md">
              <Icon as={FiTrendingUp} w={10} h={10} color="green.500" />
              <StatLabel fontSize="lg">תשואה שנתית</StatLabel>
              <StatNumber fontSize="3xl" fontWeight="bold">
                +125%
              </StatNumber>
            </Stat>
            <Stat bg={statBg} p={6} rounded="lg" shadow="md">
              <Icon as={FiLock} w={10} h={10} color="blue.500" />
              <StatLabel fontSize="lg">אבטחה</StatLabel>
              <StatNumber fontSize="3xl" fontWeight="bold">
                100%
              </StatNumber>
            </Stat>
            <Stat bg={statBg} p={6} rounded="lg" shadow="md">
              <Icon as={FiDatabase} w={10} h={10} color="purple.500" />
              <StatLabel fontSize="lg">נפח מסחר יומי</StatLabel>
              <StatNumber fontSize="3xl" fontWeight="bold">
                $2.5M
              </StatNumber>
            </Stat>
          </SimpleGrid>
        </Container>

        {/* Features Section */}
        <Box bg={useColorModeValue('white', 'gray.800')} py={20}>
          <Container maxW="container.xl">
            <VStack spacing={12}>
              <Heading textAlign="center" size="xl">
                יתרונות המערכת
              </Heading>
              <SimpleGrid columns={{ base: 1, md: 3 }} spacing={10}>
                <Feature
                  title="בוט מסחר חכם"
                  description="מערכת מסחר אוטומטית המשלבת בינה מלאכותית לזיהוי הזדמנויות"
                  icon={FiTrendingUp}
                />
                <Feature
                  title="חוזים חכמים"
                  description="מערכת חוזים חכמים מאובטחת על רשת סולנה"
                  icon={FiLock}
                />
                <Feature
                  title="אנליטיקה מתקדמת"
                  description="ניתוח נתונים בזמן אמת וויזואליזציה מתקדמת"
                  icon={FiDatabase}
                />
              </SimpleGrid>
            </VStack>
          </Container>
        </Box>
      </Box>
    </ChakraProvider>
  );
}

function Feature({ title, description, icon }: { title: string; description: string; icon: any }) {
  return (
    <VStack
      bg={useColorModeValue('white', 'gray.700')}
      p={8}
      rounded="lg"
      shadow="md"
      spacing={4}
      align="start"
    >
      <Icon as={icon} w={8} h={8} color="purple.500" />
      <Heading size="md">{title}</Heading>
      <Text color="gray.600">{description}</Text>
    </VStack>
  );
}

export default App; 